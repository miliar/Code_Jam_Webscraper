def main(filename):
    
    f = open(filename)
    res = open('res.txt', 'w')
    num_mkdir = 0
    cur_counter = 0
    case = 1
    f.readline()
    for line in f:

        line_list = line.split()
        if cur_counter == 0:
            num_exist = int(line_list[0])
            num_add = int(line_list[1])
            exist = []
            print "exist: %d\nadd: %d" %(num_exist, num_add)
        elif cur_counter <= num_exist:
            exist.append(line_list[0])
        elif cur_counter <= num_exist + num_add:
            print exist
            target = line_list[0]
            while not target == "":
                for item in exist:
                    if item == target:
                        target = ""
                        break
                if target == "":
                    break
                
                num_mkdir += 1
                exist.append(target)
                print "current target: %s" % target
                target = target[:target.rfind('/')]
            if cur_counter == num_exist + num_add:
                output = "Case #%d: %d\n" % (case, num_mkdir)
                print output
                res.write(output)
                case += 1
                num_mkdir = 0
                cur_counter = 0
                continue
        else:
            print "ERROR! cur_counter = %d" % cur_counter
            exit(0)
            
        cur_counter += 1
        

if __name__ == "__main__":
    main('A-large.in')