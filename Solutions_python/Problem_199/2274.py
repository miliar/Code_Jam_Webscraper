import random
import sys

def generate_test_data():
    cases = random.randint(5, 100)
    print "{} cases".format(cases)
    data = "{}\n".format(cases)

    for x in range(cases):
        pancakes = bin(random.getrandbits(10)).decode('ascii')[2:]
        while len(pancakes) < 2:
            pancakes = bin(random.getrandbits(10))[2:]
        spatula = random.randint(2, len(pancakes))

        pancakes = pancakes.replace('0', '-').replace('1', '+')
        data += "{} {}\n".format(pancakes, spatula)

    return data.strip()

def test(pancakes, spatula):
    max_flips = (len(pancakes) - spatula) + 1
    flipper = int("1"*spatula, base=2)
    bincakes = pancakes.replace('-', '0').replace('+', '1')
    bincakes = int(bincakes, base=2)

    flips = 0
    for i in range(max_flips):
        if bin(bincakes)[-1] == '0':
            bincakes = bincakes^flipper
            flips += 1
        bincakes = bincakes>>1

    if '0' in bin(bincakes)[2:] or len(bin(bincakes)[2:]) < spatula -1:
        return "IMPOSSIBLE"
    return flips

if __name__ == '__main__':

    if sys.argv[1] == 'gen_data':
        with open('test_data', 'w+') as outfile:
            outfile.write(generate_test_data())            
        sys.exit(1)

    infile = open(sys.argv[1])
    data = ""
    with open(sys.argv[1] + '_out', 'w+') as outfile:
        for i in range(int(infile.readline())):
            test_data = infile.readline().split(' ')
            pancakes = test_data[0]
            spatula = test_data[1]
            solution = test(pancakes, int(spatula))
            data += 'Case #{}: {}\n'.format(i+1, solution)
        outfile.write(data.strip())