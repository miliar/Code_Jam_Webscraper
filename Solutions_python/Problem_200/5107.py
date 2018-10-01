t = int(input())
a = 0

while(a<t):
    thing = 0
    num = int(input())
    for i in range(num+1):
        word = str(i)
        arr = list(word)
        if sorted(arr) == arr:
            thing = arr
    ans = ''.join(thing)
    print("Case #" + str(a+1) +":" , ans)

    a=a+1