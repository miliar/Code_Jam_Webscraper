
i = 0
t = 0
with open('test02.out', 'w') as out_file:
    for line in open('B-small-attempt0.in'):
            i = i + 1
            if i == 2:
                inputs = line.split()
                x = []
                for word in inputs:
                    x.append(float(word))
                C = x[0]
                F = x[1]
                X = x[2]
                b = X / 2
                j = 2
                a = C / 2 + X / (F + 2)
                while (b > a):
                    b = a
                    a = 0
                    for farms in range(j):
                        a = a + C/(farms * F + 2)
                    a = a + X / (j * F + 2)
                    j = j + 1
                t = t + 1
                i = 1
                statement = "Case #" + str(t) + ": " + str(b)
                out_file.write("%s\n" % statement)
            elif i == 1:
                m = int(line)            