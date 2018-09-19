import sys
googlerese = {
    ' ':' '
   ,'a':'y'
   ,'o':'e'
   ,'z':'q'
   ,'q':'z'
}



def add_text(orig, googled):
    for g,a in zip(googled,orig):
        googlerese[g] = a

def translate(text):
    ret = ""
    for c in text:
        ret += googlerese[c]
    return ret

add_text("our language is impossible to understand",
         "ejp mysljylc kd kxveddknmc re jsicpdrysi")
add_text("there are twenty six factorial possibilities",
         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
add_text("so it is okay if you want to just give up",
         "de kr kd eoya kw aej tysr re ujdr lkgc jv")
for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    print("Case #{}: {}".format(i, translate(line.rstrip())))
