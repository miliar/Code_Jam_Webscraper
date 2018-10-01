t=int(input())
for j in range(t):
    n=int(input())
    for i in range(n, 0, -1):
        orig=str(i)
        orig_sort=''.join(sorted(orig))
        if orig==orig_sort:
            print('case #',end='')
            print((j+1),end='')
            print(':',orig)
            break