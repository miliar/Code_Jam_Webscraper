input_file = "A-large.in"
output_file = input_file.replace('.in', '.out', 1)

input = open(input_file, 'r')
output = open(output_file, 'w')

T = int(input.readline())

for i in range(T):
    Smax, Si  = input.readline().split()
    Smax = int(Smax)
    
    l = map(int, list(Si))

    for a in range(Smax-1):
        if l[a] > 1: 
            l[a+1] = l[a+1] + l[a] - 1
            l[a] = 1
    c = 0
    for a in range(Smax):
        if(l[a]) == 0:
            c += 1
     
    output.write('Case #'+ str(i+1) + ': ' + str(c) + '\n')    