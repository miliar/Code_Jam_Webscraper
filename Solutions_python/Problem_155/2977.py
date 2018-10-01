num = int(raw_input());
data = [(raw_input()) for raw in range(num)]
counter = 1;
for item in data:
    temp = item.split(" ");
    level = 0;
    need = 0;
    total = 0;
    for char in temp[1]:
        if total < level:
            need += level - total;
            total += level - total;
        total += int(char);
        level += 1
    print "Case #%d: %d" %(counter, need);
    counter += 1;
    
