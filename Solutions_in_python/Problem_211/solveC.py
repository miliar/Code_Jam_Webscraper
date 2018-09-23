import math
import sys
import decimal

def read_data(filename):
    with open(filename) as f:
        cases = int(f.readline().strip())
        data = []
        for i in xrange(cases):
            cores, cores_needed = map(int, f.readline().strip().split())
            training_units = decimal.Decimal(f.readline().strip())
            cores_p = map(decimal.Decimal, f.readline().strip().split())
            data.append({
                'cores': cores,
                'cores_needed': cores_needed,
                'training_units': training_units,
                'cores_p': cores_p
            })
        return data
def increase_p_values(p_values, training_units):
    while training_units > 0:
        working_p = p_values[0]
        num_p = 1
        objective = decimal.Decimal('1.0')
        for i in range(1, len(p_values)):
            if p_values[i] > working_p:
                objective = p_values[i]
                break
            num_p += 1
        total = (objective - working_p) * num_p

        if total > training_units:
            total = training_units
        inc_p = total / num_p
        for i in range(num_p):
            p_values[i] += inc_p
        training_units -= total
    return training_units, p_values

def solveC(data):
    for case, d in enumerate(data, 1):
        d['cores_p'].sort()
        p_values = d['cores_p']
        training_units = d['training_units']
        solved = False
        while training_units > 0 and not solved:
            training_units, p_values = increase_p_values(p_values, training_units)
            solved = all(p_val == decimal.Decimal('1.0') for p_val in p_values)

        print "Case #{}: {}".format(case, reduce(lambda x, y: x * y, p_values))


if __name__ == '__main__':
    file_name = sys.argv[1]
    solveC(read_data(file_name))
