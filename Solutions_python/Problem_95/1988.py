# Python 2.5

dic = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

input=[x.strip() for x in file('A-small-attempt0.in','rb+').read().split('\n')[1:]]
output=file('A-small-attempt0.out','wb+')

for l in range(len(input)):
 o=''
 for m in input[l]: print m,; o+=dic[m]; print o
 output.write('Case #'+str(l+1)+': '+o+'\n')