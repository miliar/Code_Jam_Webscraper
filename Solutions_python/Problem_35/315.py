def read_file(filename):
    fp = open(filename)
    lines = fp.readlines()
    return lines

def topo_map(filename):
    result = ""
    lines = read_file(filename)
    t = int(lines[0])
    index = 1
    for x in range(t):
        dim = lines[index].split()
        h = int(dim[0])
        w = int(dim[1])
        m = get_map(lines, index + 1, h, w)        
        num_sinks = 0
        sink_chart = []
        for i in range(h):
            row = []
            for j in range(w):
                if sink(m, i, j):
                    num_sinks = num_sinks + 1
                    row.append(num_sinks)
                else:
                    row.append(0)
            sink_chart.append(row)
        for i in range(h):
            for j in range(w):
                sink_chart[i][j] = get_sink(m,sink_chart,i,j)
        index = index + h + 1        
        sink_chart = alphalabel(sink_chart,num_sinks)        
        result = result + "Case #" + str(x+1) + ":\n"+sink_string(sink_chart)
    return result

def sink_string(sink_chart):
    string = ""
    for i in range(len(sink_chart)):
        row = ""
        for j in range(len(sink_chart[0])):
            row = row + sink_chart[i][j] + " "
        string = string + row + "\n"
    return string

def get_sink(m, sink_chart, x, y):
    if sink_chart[x][y] > 0:
        return sink_chart[x][y]
    val = m[x][y]
    low_alt = val
    sxcor = -1
    sycor = -1
    if x > 0:
        if m[x-1][y] < low_alt:
            sxcor = x-1
            sycor = y
            low_alt = m[x-1][y]
    if y > 0:
        if m[x][y-1] < low_alt:
            sxcor = x
            sycor = y-1
            low_alt = m[x][y-1]
    if y < len(m[0]) - 1:
        if m[x][y+1] < low_alt:
            sxcor = x
            sycor = y+1
            low_alt = m[x][y+1]
    if x < len(m) - 1:
        if m[x+1][y] < low_alt:
            sxcor = x+1
            sycor = y
            low_alt = m[x+1][y]
    return get_sink(m,sink_chart,sxcor,sycor)

def alphalabel(sink_chart,num_sinks):
    labels = []
    ascii = 97
    for x in range(num_sinks+1):
        labels.append("")
    for i in range(len(sink_chart)):
        for j in range(len(sink_chart[0])):
            sink = sink_chart[i][j]
            if labels[sink] == "":
                labels[sink] = chr(ascii)
                ascii = ascii + 1
            sink_chart[i][j] = labels[sink]
    return sink_chart
            
def sink(m,x,y):
    val = m[x][y]
    if x > 0:
        if val > m[x-1][y]:
            return False
    if y > 0:
        if val > m[x][y-1]:
            return False
    if x < len(m) - 1:
        if val > m[x+1][y]:
            return False
    if y < len(m[0]) - 1:
        if val > m[x][y+1]:
            return False
    return True


def get_map(lines, index, h, w):
    m = []
    for i in range(h):
        row = []
        row_vals = lines[index + i].split()
        for j in range(w):
            row.append(int(row_vals[j]))
        m.append(row)
    return m

def run(filename):
    a = open("output.txt","w")
    a.write(topo_map(filename))

run("B-large.txt")

