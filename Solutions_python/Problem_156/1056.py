#Problem B. Infinite House of Pancakes
__author__ = 'anna'
f = open('/Users/anna/Mine/code_jam/code_jam_2015/b_sol_large', 'w')

tasks=[]
tasks_hm=[]
N=0
def read_tasks():
    with open('/Users/anna/Mine/code_jam/code_jam_2015/b_in','r') as f:
    #with open('/Users/anna/Mine/Code_Jam_2014/c_small','r') as f:
        global T
        T=int(f.readline())
        k=1
        for line in f:
            if k%2==0:
                lines=line.strip()
                tasks.append(map(int, lines.split(' ')))
            else:
                lines=line.strip()
                tasks_hm.append(int(lines))
            k += 1

def current_time(problem_list,num_eat):
    ret=0;
    for i in problem_list:
        if i%num_eat>0:
            ret+=i/num_eat
        else:
            ret+=i/num_eat - 1
    return ret+num_eat


read_tasks();
for task_iterator in range(0,T):
   # print task_iterator
    current_task=tasks[task_iterator]
  #  print current_task
    M=max(current_task)
    print
    current_min=[]
    for Peat in range(1,M+1,1):
        current_min.append(current_time(current_task,Peat))
     #   print "Peat ",Peat, "current time ",current_time(current_task,Peat)
    real_min=min(current_min)

    f.write("Case #"+ str(task_iterator+1)+": "+str(real_min)+"\n")
