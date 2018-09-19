import os, os.path


#0 = sample file (X-sample.in)
#1 = small input (X-small.in)
#2 = large input (X-large.in)
#3 = auto (large > small > sample)

def open_file(module_name, inputfile_setting = 3):
    base_name = module_name[:-3]

    type_names = ['-sample', '-small', '-large']

    in_names= [base_name+tn+'.in' for tn in type_names ]
    out_names= [base_name+tn+'.out' for tn in type_names ]
    sample_val_name= base_name+'-sample'+'.val'

    for fin_name, fout_name in reversed(zip(in_names[:], out_names[:])):
        if os.path.exists(fin_name):
            in_names.append(fin_name)
            out_names.append(fout_name)
            break
    
    if len(in_names) > inputfile_setting and os.path.exists(in_names[inputfile_setting]):
        fin = file(in_names[inputfile_setting], 'rt')
        fout = file(out_names[inputfile_setting], 'wt')
        problem_solution( fin, fout, base_name )
        fin.close()
        fout.close()
        
        if in_names[inputfile_setting] == in_names[0] and os.path.exists(out_names[0]) and os.path.exists(sample_val_name): #sample input , outpout and validation
            check_sample_solution(out_names[0], sample_val_name)
            
        
    else:
        print 'Could not find file(s)'
        return
    
    
def problem_solution(fin , fout, base_name):
    #exec('from %s import problem_testcase' %(base_name))
    from A import problem_testcase
    N = int(fin.readline().strip())
    print N
    for t in range(1, N+1):
        results = problem_testcase(fin, fout, t)
        if results!= None and (isinstance(results, list) or isinstance(results, tuple)):
            print >> fout, cnum(t), ' '.join([str(r) for r in results])


def check_sample_solution(filename_out, filename_val):
    def clean_items(line):
        items = [ item.strip() for item in line.strip().split()]
        items = [ non_null for non_null in items if non_null!='']
        for index, item in enumerate(items[:]):
            try:
                items[index] = int(item)
            except ValueError:
                try:
                    items[index] = float(item)
                except ValueError:
                    items[index] = item
        return items
    
    validated = True
    for out_l, val_l in zip(file(filename_out, 'rt').readlines(), file(filename_val, 'rt').readlines()):
        out_items = clean_items(out_l)
        val_items = clean_items(val_l)
        difference = False
        for out_item, val_item in zip(out_items, val_items):
            if isinstance(out_item, float) and isinstance(val_item, float):
                if abs(out_item - val_item) > 1e-6:
                    difference = True
                    break
            else:
                if out_item!=val_item:
                    difference = True
                    break
                    
        if difference:
            print 'Difference Spotted'
            print ' '.join([str(s) for s in out_items])
            print ' '.join([str(s) for s in val_items])
            validated = False
    
    if validated:
        print 'Correct !'
    else:
        print 'Failed Validation !'
        
        

    
def cnum(t):
    return 'Case #%d: ' % (t)
