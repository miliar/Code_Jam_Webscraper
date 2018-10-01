# imports
import sys, re

def is_int(i):
    try:
        val = int(i)
        return True
    except ValueError:
        return False

def replace_str_index(text, index=0, replacement=''):
    return "%s%s%s" % (text[:index], replacement, text[index+1:])

def main(filename):
    # open file
    f_in = open(filename, "r")
    # return array of lines
    lines = f_in.readlines()
    # close file
    f_in.close()

    #
    f_out = open("%s.out" % filename, "w")
    use_case_count = int(lines.pop(0))
    current_use_case_num = 0
    for line in lines:
        if current_use_case_num > use_case_count:
            break
        else:
            current_use_case_num += 1

        if is_int(line):
            use_case_count = int(line)
        else:
            chunks = re.split(" ", line)
            s = list(chunks[0])
            k = int(chunks[1])
            result = 0
            for index, char in enumerate(s):
                if char == "-":
                    if (index + k) <= len(s):
                        c_index = index
                        while c_index < (index + k):
                            if s[c_index] == "-":
                                s[c_index] = "+"
                            else:
                                s[c_index] = "-"
                            c_index += 1
                        result += 1
                    else:
                        result = "IMPOSSIBLE"
                        break

            f_out.write("Case #%s: %s\n" % (str(current_use_case_num), str(result)))
    f_out.close()

main("./A-large.in")


