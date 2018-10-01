import sys
import operator

def get_max_pile_value(values):
    summ = reduce(operator.xor, values)
    if summ != 0:
        return
    
    return sum(sorted(values)[1:])

def main(input, output):
    cases_count = int(input.readline())
    for i in xrange(cases_count):
        case_id = i+1
        
        case_len = int(input.readline())
        case = map(int, input.readline().split())
        assert len(case) == case_len
        
        result = get_max_pile_value(case)
        if result is None:
            result = 'NO'
        
        print >> output, 'Case #%s: %s' % (case_id, result)

if __name__ == '__main__':
    if '-q' in sys.argv:
        log = lambda msg: None
        sys.argv.remove('-q')
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = 'example.txt'
    with file(input_path) as input:
        main(input, sys.stdout)
    