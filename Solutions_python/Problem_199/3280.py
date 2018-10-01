'''flip pancacke'''

def flipBits(data,k):
    new_data = ""
    for i in range(k):
        if(data[i] == '+'):
            new_data += '-'
        else:
            new_data += '+'
    return new_data + data[k:]
        

def get_n_flip(s,n,k):
    '''flip pancacke'''
    data = s.lstrip('+')
    if len(data) == 0:
        return n;
    if len(data) < k:
        return "IMPOSSIBLE"
    data = flipBits(data,k)
    return get_n_flip(data,n+1,k)




n = input()
xs = []
for i in range(n):
    line = raw_input().split()
    xs.append(line)

for i in range(n):
    s = xs[i][0]
    k = int(xs[i][1])
    print "Case #"+str(i+1)+": "+str(get_n_flip(s,0,k))
