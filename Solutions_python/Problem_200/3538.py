#f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/input2', 'r')
# C:\Users\Avinash\Desktop\Google codejam 2017\pycharmworks\AA-small-practice.in
# f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/A-large-practice.in', 'r')
f = open('C:/Users/Avinash/Desktop/Google codejam 2017/pycharmworks/B-small-attempt0.in', 'r')
data = f.readlines()
f.close()
f = open('tidy2', 'w')
t = data[0]
y = 0
for i in data[1:]:
    y += 1
    number = int(i)
    stringnumber = str(number)
    string1 = ""
    for j in range(len(stringnumber) - 1):
        ten = int(stringnumber[j])
        if stringnumber[j] > stringnumber[j + 1]:
            string1 = str(ten - 1)
            for k in range(j, len(stringnumber) - 1):
                string1 += "9"
            stringnumber = stringnumber[:j] + string1

        if stringnumber[j] == stringnumber[j + 1]:
            try:
                for k in range(j, len(stringnumber)):
                    if stringnumber[j] > stringnumber[k]:
                        string1 = str(ten - 1)
                        for x in range(j, len(stringnumber) - 1):
                            string1 += "9"
                        stringnumber = stringnumber[:j] + string1

            except:
                continue

    count = (int(stringnumber))
    print(count)
    print("Case #" + str(y) + ": " + str(count), file=f)

f.close()
