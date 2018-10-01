#!/usr/bin/python


input_file = open('C-small-attempt1.in')
output_file = open('output', 'w')

T = int(input_file.readline())

phrase = 'welcome to code jam'

def remove_chars(text, chars):
    for c in chars:
        text = text.replace(c, '')
    return text

def remove_multis(text):
    factor = 1
    old_c = ''
    new_text_array = []
    for c in text:
        if c != old_c:
            new_text_array.append(c)
            old_c = c
        else:
            factor *= 2
    return ''.join(new_text_array), factor


def rek(phrase_i, text_i,):
    global count
    while text_i < len(text):
        while phrase[phrase_i] != text[text_i]:
            text_i += 1
            if text_i == len(text):
#                break
                return
        if phrase_i == len(phrase) - 1:
            count += 1
            if count == 10000:
                count = 0
#            return
        if phrase_i < len(phrase) - 1:
            rek(phrase_i + 1, text_i + 1)
        text_i += 1

for t in range(T):
    text = input_file.readline().rstrip("\n")

    text = remove_chars(text, 'bfghiknpqrsuvxyz')
#    text, factor = remove_multis(text)

    count = 0
    rek(0, 0)

#    dddd = str(count * factor).zfill(4)[-4:]
    dddd = str(count).zfill(4)

    output_file.write("Case #" + str(t + 1) + ": " + dddd + "\n")

input_file.close()
output_file.close()
