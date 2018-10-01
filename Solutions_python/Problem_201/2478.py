#f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/input2', 'r')
# C:\Users\Avinash\Desktop\Google codejam 2017\pycharmworks\AA-small-practice.in
# f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/A-large-practice.in', 'r')
f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/C-small-1-attempt0.in', 'r')
# f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/B-large.in', 'r')
data = f.readlines()
f.close()
f = open('bathroom2', 'w')
t = data[0]
y = 0
for i in data[1:]:
    y += 1
    count = 0
    out = [item for item in i.split(' ')]
    number = int(out[0])
    people = int(out[1])
    array = [number]
    for j in range(people):
        x = max(array)
        if x % 2 == 0:
            a = int(x / 2) - 1
            b = x - a - 1
        else:
            a = int(x / 2)
            b = x - a - 1

        array.remove(x)
        array.extend((a, b))
        # print(array)
    m = max(a, b)
    n = min(a, b)
    #print(m,n)
    print("Case #" + str(y) + ": " + str(m) + " " + str(n), file=f)

f.close()
