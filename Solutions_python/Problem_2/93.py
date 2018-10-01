def get_file_lines():
    ret = []
    f = open('cases.txt','r')

    for line in f:
        ret += [line.strip()]

    f.close()
    return ret

def get_file_text():
    f = open('cases.txt','r')
    ret = f.read()
    f.close()
    return ret

def get_file_input():
    ret = []
    f = open('cases.txt','r')

    for line in f:
        ret += [map(float,line.strip().split(' '))]

    f.close()
    return ret

def output(text):
    print text
    f = open('result.txt', 'w+')
    f.write(text)
    f.close()


#    for line in get_file_lines():
#        print line