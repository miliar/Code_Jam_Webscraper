
import sys
import string

def resolve_jam():
    speech_in  = 'ejp mysljylc kd kxveddknmc re jsicpdrysi\n'
    speech_in += 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n'
    speech_in += 'de kr kd eoya kw aej tysr re ujdr lkgc jv (qz)\n'
    speech_out  = 'our language is impossible to understand\n'
    speech_out += 'there are twenty six factorial possibilities\n'
    speech_out += 'so it is okay if you want to just give up (zq)\n'

    table_in, table_out = '', ''
    notfinded_in, notfinded_out = string.lowercase, string.lowercase


    #print "Length of speech_in  : %d" % len(speech_in)
    #print "Length of speech_out : %d" % len(speech_out)

    for i in range(len(speech_in)):
        l_in = speech_in[i]
        l_out = speech_out[i]
        if not l_in in table_in and l_in in string.letters:
            table_in += l_in
            table_out += l_out
            notfinded_in = notfinded_in.replace(l_in, '')
            notfinded_out = notfinded_out.replace(l_out, '')

    #print "Table in  : %s (len: %d)" % (repr(table_in), len(table_in))
    #print "Table out : %s (len: %d)" % (repr(table_out), len(table_out))

    trans_tab = string.maketrans(table_in, table_out)
    #print "Translate Table : %s" % repr(trans_tab)

    trans_out = speech_in.translate(trans_tab)
    #print "Speech_in:\n%s" % speech_in
    #print "Speech_out:\n%s" % trans_out

    #print "Not Finded in  :\n%s" % repr(notfinded_in)
    #print "Not Finded out :\n%s" % repr(notfinded_out)
    return trans_tab

    
def do_it():
    all_tc = sys.stdin.readlines()
    trans_tab = resolve_jam()

    for tc_n in range(1, int(all_tc[0])+1):
        print "Case #%d: %s" %(tc_n, all_tc[tc_n].translate(trans_tab).strip())

if __name__ == '__main__':
    do_it()

