# -*- coding: utf-8 -*-

import sys

def _result(check):
    for item in check:
        if item.count("X") == 4:
            return "X won"
        elif item.count("X") == 3 and "T" in item:
            return "X won"
        elif item.count("O") == 4:
            return "O won"
        elif item.count("O") == 3 and "T" in item:
            return "O won"
            
    for item in check:
        if "." in item:
            return "Game has not completed"
            
    return "Draw"
    

in_file = sys.argv[1]
out_file = in_file.replace(".in", ".out")

f_in = open(in_file, "rt")
f_out = open(out_file, "wt")

case = 1
lines = []
check = []

next(f_in)

for line in f_in:
    line = line.strip()
    
    if len(line) <= 0:
        continue
    else:
        lines.append(line)
        
        if len(lines) >= 4:
            check = lines[:]

            for i in range(0, 4):
                buf = ""
                
                for j in range(0, 4):
                    buf += lines[j][i]
                    
                check.append(buf)
                
            check.append(lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3])
            check.append(lines[0][3] + lines[1][2] + lines[2][1] + lines[3][0])
            
            res = _result(check)
            
            print("Case #%s: %s" % (case, res))
            f_out.write("Case #%s: %s\n" % (case, res))
            
            lines = []
            check = []
            
            case += 1

f_in.close()
f_out.close()
