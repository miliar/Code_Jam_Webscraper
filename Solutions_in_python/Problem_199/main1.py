def s_print(v):
    ss = ''
    for vv in v:
        if vv:
            ss+='+'
        else:
            ss += '-'
    print(ss)
    
def f(s,k):
 #   print('f for {} {}'.format(s,k))
    k = int(k)
    l = []
    ss = []
    for i in range(len(s)):
        if s[i] == '+':
            l.append(True)
        else:
            l.append(False)
        ss.append(True)

 #   s_print(l)
 #  s_print(ss)
    count = 0

    try:
     #   print('starting to flip')
        for i in range(len(l)):
            
            #s_print(ss)
            if l[i] != ss[i]:
                count += 1
                for j in range(i,i+k):
                    ss[j] = not ss[j]
    except IndexError:
        return 'IMPOSSIBLE'

    return count 

#input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s,k = input().split(" ")  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, f(s,k)))
