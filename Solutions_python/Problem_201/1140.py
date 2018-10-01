
from math import ceil
from math import floor

def most_significent_bit(n):
    m = n
    m = m | m >> 1
    m = m | m >> 2
    m = m | m >> 4
    m = m | m >> 8
    m = m | m >> 16
    m = m | m >> 32
    return m & ~(m >> 1)

def go_left(stalls):
    return ceil((stalls - 1)/2.0)

def go_right(stalls):
    return floor((stalls - 1)/2.0)


def bathroom_stalls(stalls, people):
    result = stalls
    max = most_significent_bit(people) 
    
    m = 1

    while m < max and max != 0:
        if people & m :
            result = go_right(result)
        else:
            result = go_left(result)
        m = m << 1

    return go_left(result), go_right(result)
        


def main():
    """ main function """
    number_of_lines = int(input())
    for n in range(1, number_of_lines + 1):
        line = input().split()
        stalls = int(line[0])
        people = int(line[1])
        result = bathroom_stalls(stalls, people)
        print("Case #"+str(n)+": " + str(result[0]) + " " +str(result[1]))


if __name__ == "__main__":
    main()

