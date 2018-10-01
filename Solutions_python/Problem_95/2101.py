# define our method
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

f = open('A-small-attempt1.in').readlines()
## Read the first line
line = f.pop(0)
i=0
for line in f:
     i=i+1
     reps= {'a': 'Y','b': 'H','c': 'E','d': 'S','e': 'O','f': 'C','g': 'V','h': 'X','i': 'D','j': 'U','k': 'I','l': 'G','m':'L','n': 'B','o': 'K','p': 'R','q': 'Z','r': 'T','s': 'N','t': 'W','u': 'J','v': 'P','x': 'M','y': 'A','z': 'Q','w': 'F'}

     line = replace_all(line, reps)

     reps= {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}

  
     line = replace_all(line, reps)

     text_file = open("output.txt", "a")

     text_file.write('Case #' + str(i) + ': '+line)

     line = open('A-small-attempt0.in').readlines()
open('A-small-attempt0.in').close()
