
f = file('cipher')
string_mapping = []
char_mapping = {}

x = int(f.readline())
for i in range(x):
    string_mapping.append([f.readline()])

for i in range(x):
    string_mapping[i].append(f.readline())

for i in range(x):
    for j in range(len(string_mapping[i][0])):
        x1 = string_mapping[i][0][j]
        x2 = string_mapping[i][1][j]
        char_mapping[x1] = x2

char_mapping['z'] = 'q'
char_mapping['q'] = 'z'
#print sorted(char_mapping.keys())
f = file('input')
x = int(f.readline())

for i in range(x):
    s = f.readline()
    s_list = [ char_mapping[x] for x in s]
    s_out = "".join(s_list)
    print "Case #%s: %s" % (str(i + 1), s_out),
