from shlex import split

def read_file():
    f = open("qb_in.txt")
    global a
    a = f.readlines()
    global test_cases
    assert int(a[0])
    test_cases = int(a.pop(0))
    a = [s.strip("\n") for s in a]
    f.close()
    
def convert_data():
    global data
    data = []
    global sims
    sims = []
    global results
    results = []
    curr_line = -1 # popped the first one
    for i in range(test_cases):
        data.append([])
        sims.append([])
        curr_line += 1
        if int(split(a[curr_line])[0]) == 0 or int(split(a[curr_line])[1]) == 0:
            results.append("YES")
            continue
        for j in range(int(split(a[curr_line])[0])): # assume Google doesn't fsck up
            curr_line += 1
            num_array = split(a[curr_line])
            num_array = [int(s) for s in num_array]
            data[i].append(num_array)
            sims[i].append([])
            for k in range(len(num_array)):
                sims[i][j].append(100)

def make_value_list(d):
    global value_list
    value_list = []
    for row in d:
        for point in row:
            value_list.append(point)
    value_list = list(set(value_list))
    value_list.sort()
    value_list = value_list[::-1]

def find_lower_maxi():
    global maxi_index
    global maxi
    if maxi_index < len(value_list):
        maxi = value_list[maxi_index]
        maxi_index += 1
        return True

def cut_single(s, d, ly, lx):
    lrow = []
    lcol = []
    for y in range(len(d)):
        for x in range(len(d[y])):
            if y == ly:
                lrow.append(d[y][x])
            if x == lx:
                lcol.append(d[y][x])
                
    to_cut = ["x-axis", "y-axis"]
    for num in lrow:
        if maxi < num:
            to_cut.pop(0)
            break
    for num in lcol:
        if maxi < num:
            to_cut.pop(to_cut.index("y-axis"))
            break
            
    for cut in to_cut:
        if cut == "x-axis":
            for oxo in range(len(s[ly])):
                if s[ly][oxo] > maxi:
                    s[ly][oxo] = maxi
        if cut == "y-axis":
            for y in range(len(s)):
                if s[y][lx] > maxi:
                    s[y][lx] = maxi
            
            
            

def cut_all(s, d):
    for y in range(len(s)):
        for x in range(len(s[y])):
            if s[y][x] > maxi >= d[y][x]:
                cut_single(s, d, y, x)

def is_done(s, d):
    if s == d:
        return True      

"""def check_grass():
        maxi = 100
        for y in range(len(data[d])):
            sols[d].append([])
            for x in range(len(data[d][y])):
                sols[d][y].append(check_neighbours(data[d], y, x))"""
    

def write_to_file():
    f2 = open("qb_out.txt", 'wt') 
    for i in range(len(results)):
        f2.writelines("Case #"+str(i+1)+": "+str(results[i])+"\n")   
    f2.close()

def debug():
    print data
    print sims # simulations
    print results

def main():
    global results
    read_file()
    convert_data()
    for d in data:
        s = sims[data.index(d)]
        make_value_list(d)
        global maxi
        maxi = 101
        global maxi_index
        maxi_index = 0
        while find_lower_maxi() and s != d:
            cut_all(s, d)
        if s == d:
            results.append("YES")
        else:
            results.append("NO")      
    write_to_file() # < check first for rows, then completion
    #debug()

if __name__ == "__main__":
    main()
