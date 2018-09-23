
# coding: utf-8

# In[16]:

input_file = r"C:\Users\frame\Downloads\A-large.in"
output_file = input_file.replace(".in",".out")


# In[17]:

def get_tasks():
    with open(input_file, "r") as f:
        lines = f.read().split("\n")
        n, content = int(lines[0]), lines[1:-1]

    tasks = [(list(s), int(k)) for s,k in [l.split(" ") for l in content]]
    assert(len(tasks) == n)
    return tasks


# In[18]:

def flip(s, pos, k=3):
    def flip_single(s, p): 
        s[p] = "+" if s[p] is "-" else "-"
    for i in range(k):
        flip_single(s, pos+i)
    return s


# In[19]:

def solve(task, k):
    pos = i =0
    for i in range(len(task)):
        if not "-" in task:
            return i
        pos = task.index("-")
        if pos>len(task)-k:
            return "IMPOSSIBLE"
        flip(task, pos, k)


# In[20]:

result = ""
for i, (s, k) in enumerate(get_tasks()):
    res = solve(s,k)
    string = "Case #%i: %s"%(i+1, res)
    result += "%s\n"%string
    print(string)


# In[15]:

with open(output_file, "w") as f:
    f.write(result)


# In[ ]:



