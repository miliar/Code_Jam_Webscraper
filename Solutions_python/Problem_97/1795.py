fob = open('c:/Users/Nemanja/Documents/python/Recycled Numbers/C-small-attempt0.in', 'r');
cases = int(fob.readline());
output = [];
for case in range(1,cases+1):
    line = fob.readline();
    line = line.split();
    a = int(line[0]);
    b = int(line[1]);
    lenght = len(str(a));
    counter = 0;
    for n in range (a,b):
        for m in range (b,a,-1):
            for x in range (1, lenght):
                n1 = n%10**x;
                tmp = n/10**x;
                a1 = n1*10**(lenght-x)+tmp;
                if a1 == m and n<m:
                    counter += 1;
    output.append("Case #" + str(case) + ": " + str(counter) + "\n");
fob.close();
fob = open('c:/Users/Nemanja/Documents/python/Recycled Numbers/output.txt', 'w');
fob.writelines(output);
fob.close();
