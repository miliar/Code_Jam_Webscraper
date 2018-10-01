inputfile = open('A-large.in', 'r')
T = int(inputfile.readline())
output = open("output2.txt", 'w')


for i in range(1,T+1):
    arr = inputfile.readline()
    pancakes,k= arr.strip().split(' ')
    pancakes, k =list(pancakes),int(k)
    rep = 0


    def flip(pancakes, k):
        global rep
        rep += 1
        for cake in range(k):
            if pancakes[cake] == '+':
                pancakes[cake] = '-'
            else:
                pancakes[cake] = '+'

    while len(pancakes) >= k:
        if pancakes[0] == '-':
            flip(pancakes,k)
        pancakes.pop(0)
    if ('-' in pancakes):
        rep = "IMPOSSIBLE"
    output.write('Case #%d: %s\n' % (i, str(rep)))
