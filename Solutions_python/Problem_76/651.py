import sys
from itertools import combinations
from operator import xor
VERBOSE =  0
def resolve(num_list):
    best_so_far = 0
    candy_sum = sum(num_list)
    # i is the number of candies for patrick
    for i in range(1, len(num_list)/2+1):
        for patrick_candy in combinations(num_list, i):
            sean_candy = num_list[:]
            for candy in patrick_candy:
                sean_candy.remove(candy)
            #if len(patrick_candy) == 1 and reduce(xor, sean_candy) == patrick_candy[0] \
            if reduce(xor, patrick_candy) == reduce(xor, sean_candy):
                patrick_sum = sum(patrick_candy)
                sean_sum = candy_sum - patrick_sum
                if sean_sum > best_so_far:
                    best_so_far = sean_sum
                if VERBOSE:
                    print 'find one solution: '
                    print 'Patrick candies: ', patrick_candy
                    print 'Sean candies: ', sean_candy
                    print 'Patrick Sum: ', patrick_sum
                    print 'Sean Sum: ', sean_sum
                    print 'Patrick thinks sum: ', reduce(xor, sean_candy)
    if best_so_far == 0:
        best_so_far = 'NO'
    return best_so_far
    
def main():
    file = open(sys.argv[1])
    length = file.readline()
    case_num = 1
    while True:
        count = file.readline()
        num_str = file.readline().strip()
        if not num_str:
            break
        num_list = [int(elem) for elem in num_str.split(' ')]
        if VERBOSE:
            print '-' * 20
            print num_list
        result = resolve(num_list)
        print 'Case #%d: %s' %(case_num, result) 
        case_num += 1

if __name__ == '__main__':
    main()
