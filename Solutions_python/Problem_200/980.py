
def largest_tidy_number(num):
    if num < 10:
        return num
    st = str(num)
    while int(st) > 0:
        n = len(st)
        for i in range(n-1):
            if int(st[i]) > int(st[i+1]):
                temp = ''
                try:
                    temp = st[:i]
                except:
                    pass
                temp += str(int(st[i])-1)+"9"*(n-i-1)
                st = temp
                break
            else:
                if n == i+2:
                    return long(st)



def main():
    f = open('B-small-attempt0.in','r')
    out = open('te.txt','w')
    for i in range(int(f.readline())):
        out.write('Case #'+str(i+1)+": "+str(largest_tidy_number(int(f.readline())))+'\n')
    out.close()



if __name__ == '__main__':
    main()

