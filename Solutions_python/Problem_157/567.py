import sys

QUATRO = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k', '-1': '-1', '-i': '-i', '-j': '-j', '-k': '-k'},
          'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j', '-1': '-i', '-i': '1', '-j': '-k', '-k': 'j'},
          'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i', '-1': '-j', '-i': 'k', '-j': '1', '-k': '-i'},
          'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1', '-1': '-k', '-i': '-j', '-j': 'i', '-k': '1'},
          '-1': {'1': '-1', 'i': '-i', 'j': '-j', 'k': '-k', '-1': '1', '-i': 'i', '-j': 'j', '-k': 'k'},
          '-i': {'1': '-i', 'i': '1', 'j': '-k', 'k': 'j', '-1': 'i', '-i': '-1', '-j': 'k', '-k': '-j'},
          '-j': {'1': '-j', 'i': 'k', 'j': '1', 'k': '-i', '-1': 'j', '-i': '-k', '-j': '-1', '-k': 'i'},
          '-k': {'1': '-k', 'i': '-j', 'j': 'i', 'k': '1', '-1': 'k', '-i': 'j', '-j': '-i', '-k': '-1'}}

def run_test(case_number, generator):
    letters, repeats = [int(x) for x in next(generator).split()]
    array = list(next(generator)[:-1]) * repeats
    i_current = '1'
    possible_i = [] 
    possible_k = [] 
    for i in range(len(array)):
        i_current = QUATRO[i_current][array[i]]
        if i_current == 'i':
            possible_i.append(i)
    k_current = '1'
    for k in range(1, len(array) - 1):
        k_current = QUATRO[array[len(array) - k]][k_current]
        if k_current == 'k':
            possible_k.append(len(array) - k)
    for pi in possible_i:
        j_current = '1'
        last_pk = pi + 1
        for pk in possible_k:
            if pk <= pi:
                continue
            for j in range(last_pk, pk):
                j_current = QUATRO[j_current][array[j]]
            last_pk = pk
            if j_current == 'j':
                print('Case #%d: YES' % case_number)
                return
    print('Case #%d: NO' % case_number)

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()