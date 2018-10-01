sample = open('A-small-attempt1.in', 'r')
text = sample.readlines()

print text

n_set= text[0]
n= int(n_set)

dictionary = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o',
              'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u',
              'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k',
              'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w',
              'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '}

outfile = open('tonguesout4.txt', 'w')

print n

for count in xrange(1, n+1):
    phrase = text[count]
    english_text = []
    for character in phrase[:-1]:
        english_text.append(dictionary[character])
    print ''.join(english_text)
    outfile.write("Case #%d: %s\n" %(count, ''.join(english_text)))
outfile.close()
        
