t = int(input())
def flip(li , i):
    x = li[i]
    if (x == '+'):
        li[i] = '-'
    else:
        li[i] = '+'

def flip_row(li , p ,k):
    for i in range(p, p+k):
        flip(li , i)

def find_minus(li):
    for i in range(len(li)):
        if (li[i] == '-'):
            return i
    return -1

def num_of_flip(li, k):
    i = find_minus(li)
    num = 0
    con = i + k
    while (con <= len(li) and i != -1):     
        flip_row(li,i,k)
        num += 1
        i = find_minus(li)
        con = i + k
    for item in li:
        if (item == '-'):
            return "IMPOSSIBLE"
    return num

for i in range(1, t + 1):
    n, k = input().split(" ")
    k = int(k)
    n = list(n)
    anw = num_of_flip(n,k)
    print("Case #{}: {}".format(i, anw))