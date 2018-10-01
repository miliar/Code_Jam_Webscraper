
def main(n):
    for i in range((len(n)-1),0,-1):
        if n[i] < n[i-1]:
            n[i-1] -=1
            for j in range(i, len(n)):
                n[j] = 9

    for i in n:
        if i == 0:
            n.pop(i)
        else:
            break

    answer = ''.join(str(e) for e in n)
    return(answer)



lines = int(input())
for i in range(1, lines + 1):
    n = list(input())
    n = list(map(int, n))
    result = main(n)
    print("Case #{}: {}".format(i, result))