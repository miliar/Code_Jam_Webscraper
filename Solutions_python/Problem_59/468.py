
root = {}
count = 0

def go(path, calc):
    global count
    
    def deep(current, items, calc):
        global count
        if items:
            first = items[0]                          
            item = current.get(first, None)
            temp = None
            if item:
                temp = item
            else:
                temp = {'xxxxxxxxx5454654654654xxxxx': 1}
                if calc:
                    count += 1
                current[first] = temp
            deep(temp, items[1:], calc)
            
    
    parts = filter(lambda item: item, path.split("/"))
    deep(root, parts, calc)




f = open("c:/pyvas.in")
f2 = open("c:/rez.txt", "w")
lines = map(lambda line: line.strip(), f.readlines())
test_count = int(lines.pop(0))

for i in range(test_count):
    root = {}
    count = 0
    n, m = map(int, lines.pop(0).split(" "))

    for a1 in range(n):
        go(lines.pop(0), False)
    for a2 in range(m):
        go(lines.pop(0), True)
    print count
    answer = "Case #%d: %d\n" % (i + 1, count)
    f2.write(answer)

f2.close()
print "Done"


