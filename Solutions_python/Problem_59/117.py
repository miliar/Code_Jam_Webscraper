def add_path(root,dnames,n):
    if n == len(dnames):
        return
    curr = dnames[n]
    if curr not in root:
        root[curr] = {}
    add_path(root[curr],dnames,n+1)

def count_nodes(root):
    count = 1
    for k,v in root.iteritems():
        child_count = count_nodes(v)
        #print k,child_count
        count += child_count
    return count

def handle_case(existing_paths,new_paths):
    root = {}
    for p in existing_paths:
        add_path(root,p,0)
    initial_count = count_nodes(root)
    #print root,initial_count
    for p in new_paths:
        add_path(root,p,0)
    final_count = count_nodes(root)
    #print root,final_count
    return final_count - initial_count

def parse_cases(infile):
    n = int(infile.readline())
    for i in range(n):
        nold,nnew = map(int,infile.readline().split())
        old = []
        new = []
        for j in range(nold):
            old.append(infile.readline().strip().split('/')[1:])
        for j in range(nnew):
            new.append(infile.readline().strip().split('/')[1:])
        print "Case #%d: %d" % (i+1,handle_case(old,new))

if __name__ == "__main__":
    s = """3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b"""
    #import StringIO
    #buf = StringIO.StringIO(s)
    import sys
    buf = open(sys.argv[1])
    parse_cases(buf)
    buf.close()
