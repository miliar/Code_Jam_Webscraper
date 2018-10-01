t = input()
dic = {'a': 'y', 'b': 'h', 'c':'e', 'd': 's', 'e':'o', 'f':'c', 'g':'v', 'h':'x',\
    'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r',\
    'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', \
    'y':'a', 'z':'q'}
for testnumber in range(t):
    s = raw_input()
    after = ''
    for i in range(len(s)):
        if s[i] in dic.keys():
            after += dic[s[i]]
        else:
            after += s[i]
    print "Case #" + str(testnumber+1) + ": " + after

    
