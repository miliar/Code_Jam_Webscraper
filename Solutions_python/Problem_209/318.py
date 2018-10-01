from math import pi

r = []
h = []
side = []
max_r = 0

if __name__ == '__main__':
    
    with open('in.txt', 'r') as file:
        test_cases = int(file.readline())

        for case_no in range(test_cases):

            n, k = (int(inp) for inp in file.readline().split())

            for i in range(n):
                
                ri, hi = (int(inp) for inp in file.readline().split())
                r.append(ri)
                h.append(hi)
                side.append(2 * pi * r * h)
                
