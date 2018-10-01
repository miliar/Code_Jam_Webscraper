text = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''

plaintext = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
'''

subs = {}
for i in range(len(text)):
    subs[text[i]] = plaintext[i]

subs['z'] = 'q'
subs['q'] = 'z'
lines = open('input.txt').readlines();
size = int(lines[0])
lines = lines[1:]
for i in range(size):
    line = lines[i]
    ans = ''
    for j in range(len(line)):
        ans += subs[line[j]]
    print("Case #{}: {}".format(i+1, ans), end='');
