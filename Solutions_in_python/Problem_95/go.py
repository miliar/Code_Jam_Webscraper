'''
Created on 14/04/2012

@author: ogonbat
'''
import os
import fileinput

if __name__ == '__main__':
    dict_correspondence = {}
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    i = 0
    string_one = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    string_two = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    string_tree = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    
    solved_one = "our language is impossible to understand"
    solved_two = "there are twenty six factorial possibilities"
    solved_tree = "so it is okay if you want to just give up"
    
    now_string_one = string_one.replace(' ','')
    for c in now_string_one:
        if not dict_correspondence.has_key(c):
            new_solved = solved_one.replace(' ', '')
            dict_correspondence[c] = new_solved[i]
        i += 1
        
    i = 0
    now_string_two = string_two.replace(' ','')
    for d in now_string_two:
        if not dict_correspondence.has_key(d):
            new_solved = solved_two.replace(' ', '')
            dict_correspondence[d] = new_solved[i]
        i += 1      
    i = 0
    
    now_string_tree = string_tree.replace(' ','')
    for e in now_string_tree:
        if not dict_correspondence.has_key(e):
            new_solved = solved_tree.replace(' ', '')
            dict_correspondence[e] = new_solved[i]
        i += 1
    dict_correspondence["z"] = "q"
    dict_correspondence["q"] = "z"
    init_line = 0
    file_output = open(os.path.join(SITE_ROOT,'output.in'),"w")
    final_string = ""
    for line in fileinput.input(os.path.join(SITE_ROOT,'A-small-attempt2.in')):
        if init_line != 0:
            final_string = "Case #%d: "%(init_line)
            for c in line:
                if not c.isspace():
                    if dict_correspondence.has_key(c):
                        final_string += dict_correspondence[c]
                    else:
                        print c
                        final_string += c
                else:
                    final_string += " "
        init_line += 1
        file_output.write(final_string+"\r\n")
    file_output.close()
    
    '''
    googlener = "sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremue laudantium totam rem aperiam eaue ipsa uae ab illo inventore veritatis et uasi architecto beatae vitae dicta"
    other_final = ""
    for c in googlener:
        if not c.isspace():
            get_key = [k for k, v in dict_correspondence.iteritems() if v == c][0]
            other_final += get_key
        else:
            other_final += " "
    print googlener
    print other_final
    
    
    googlener = "ui gode articulo preparation ma ha responder auxiliary summarios ui web initialmente representantes secundarimente tu pan campo programma es de uso medical westeuropee ue ma terra super synonymo al ample technic professional nos"
    other_final = ""
    for c in googlener:
        if not c.isspace():
            #print c
            get_key = [k for k, v in dict_correspondence.iteritems() if v == c][0]
            other_final += get_key
        else:
            other_final += " "
    print googlener
    print other_final
    
    final_string = ""
    for c in other_final:
        if not c.isspace():
            final_string += dict_correspondence[c]
        else:
            final_string += " "
    print final_string
    '''