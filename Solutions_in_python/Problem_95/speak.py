import json
import string

d = json.loads(open('dic', 'r').read())

def convert(str):
    trans = ''
    for i in range(len(str)):
        if str[i] in string.ascii_lowercase + string.ascii_uppercase:
            trans += d[str[i]]
        else:
            trans += str[i]
    return trans


def main():
    for i in range(input()):
        str = raw_input()
        print 'Case #%d: %s' % (i+1, convert(str))

if __name__ == '__main__':
    main()
