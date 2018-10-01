import string
table = string.maketrans(
    "ynficwlbkuomxsevzpdrjgthaq", "abcdefghijklmnopqrstuvwxyz"
)
def trans(text):
    return text.translate(table)

input_file = open('A-small-attempt0.in')
output_file = open('AresultsSmall.txt', 'w')

count = 1
l = []

for i in input_file:
    l.append(i)
li = l[1:]

for line in li:
    answer = trans(line)
    count = str(count)
    output_file.write("Case #"+count+": "+str(answer))
    count = int(count)
    count += 1



input_file.close()
output_file.close()
