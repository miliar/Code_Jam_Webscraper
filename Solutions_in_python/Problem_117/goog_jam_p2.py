def mark_possible(lawn, markup, path):
    lowest_setting = max([lawn[r][c] for r,c in path])
    for spot in path:
        r,c = spot
        if lawn[r][c] == lowest_setting:
            markup[r][c] = True

def mark_everything(lawn, markup, paths):
    for path in paths:
        mark_possible(lawn, markup, path)

def gen_paths(h,w):
    lines = []
    for i in range(w):
        lines.append(zip(range(h),[i]*h))
    for i in range(h):
        lines.append(zip([i]*w,range(w)))
    return lines

def gen_markup(h,w):
    markup = []
    for i in range(h):
        markup.append([False]*w)
    return markup

def is_possible(markup):
    for row in markup:
        if False in row:
            return "NO"
    return "YES"

inputFile = "B-large.in"
outputFile = "goog_code_jam2.out"

outputs = []

with open(inputFile) as f:
    T = int(f.readline())
    for i in range(T):
        h, w = [int(x) for x in f.readline().split()]        
        paths = gen_paths(h,w)
        markup = gen_markup(h,w)
        
        lawn = []
        for j in range(h):
            line = f.readline()
            lawn.append([int(x) for x in line.split()])

        mark_everything(lawn, markup, paths)
        p = is_possible(markup)
        outputs.append(p)

with open(outputFile, 'w') as out:
    for i, o in enumerate(outputs):
        out.write("Case #{0}: {1}\n".format(i+1,o))
