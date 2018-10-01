f = open ('B-small-attempt0.in', 'r');

def getNum():
    n = int(f.readline());
    return n;

def getLine():
    s = f.readline();
    return s[:-1];

def getLines(splitter=" "):
    l = f.readline()[:-1];
    l = l.split(splitter);
    return l;

def getNums(splitter=" "):
    l = f.readline()[:-1];
    l = l.split(splitter);
    l = list(map(int, l));
    return l;
##new code below this line





def main():
    
    vals = getNums();
    n = vals[0];
    vals = vals[1::2];

    data = {'R': vals[0], 'Y': vals[1], 'B':vals[2]};
    inverse = [(value, key) for key, value in data.items()]
    orig = max(inverse)[1];
    prev = orig;
    result = orig;
    data[orig] -= 1;
    
    while (len(result) < n):
        mx = 0;
        sel = '';
        for key, val in data.items():
            if key != prev:
                if val > mx:
                    mx = val;
                    sel = key;
        if sel == '':
            print ("IMPOSSIBLE");
            return "IMPOSSIBLE";
        if data[orig] == mx:
            if orig != prev:
                sel = orig;

        result += sel;
        prev = sel;
        data[sel] -= 1;
    if result[0] == result[-1]:
        print ("IMPOSSIBLE")
        return "IMPOSSIBLE";
    return result;

##newcode above this line

output = "";
cases = getNum();
for case in range(1, cases+1):
    output += "Case #" + str(case) + ": ";
    output += str(main());
    output += "\n";

with open('B-small.out', 'w') as o:
    o.write(output)
