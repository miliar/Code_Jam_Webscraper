import math
def main():
    fout = open("bullseye.out",'w')
    with open("bullseye.in",'r') as fin:
        case_numbers = int(fin.readline().strip())
        for i in range(case_numbers):
            r,t = map(int,fin.readline().split())
            c=0
            j=1
            a = 2*r+ 1
            while t >= a:
                t = t - a
                c += 1
                a += 4
            fout.write("Case #{}: {}\n".format(i+1,c))
        fout.close()
if __name__ == '__main__':
    main()
