inp = open("input.txt", "r")
out = open("output.txt", "w")

line = inp.readline()
case = 1
line_num = 1
bigkey = {'a': 'y', 'e': 'o', 'j': 'u', 'm': 'l', 'o': 'k', 'p': 'r', 's': 'n',
'y':'a', 'z':'q', ' ':' ', 'l':'g', 'c':'e','k':'i', 'd':'s', 'x':'m', 'v':'p',
'n':'b', '\n':'\n','r':'t', 'i':'d', 'b':'h', 't':'w', 'h':'x', 'g':'v', 'u':'j',
'w':'f', 'f':'c', 'q':'z'}
for line in inp:
    newline = []
    if line[0] == '\n':
        continue
    for char in line:
        newline.append(bigkey.get(char, '#'))
    newline = "".join(newline)
    out.write("Case #{0}: {1}".format(line_num, newline))
    line_num += 1
    
