def build_num(list_of_digits,num_base,nums):
	local_list_of_digits = list(list_of_digits)
	if( len(local_list_of_digits) == 0 ):
		nums.append(num_base)
		return
	these_digits = local_list_of_digits.pop()
	if( len(local_list_of_digits) == 0 ):
		for i in these_digits:
			build_num( local_list_of_digits, num_base + str(i),nums )
	else: #This was my attempt to double the for loops to halve overall recursion depth in attempts to improve performance
		for i in these_digits:
			local_list_of_digits2 = list(local_list_of_digits)
			these_digits_2 = local_list_of_digits2.pop()
			for j in these_digits_2:
				build_num( local_list_of_digits2, num_base + str(i) + str(j), nums )


def check_trial( num ):
	if( num != num[::-1] ):
		return False
	int_num = int(num)
	trial_sq = str(int_num * int_num)
	return (trial_sq == trial_sq[::-1])

# Use patterns for these palindromic numbers to build the list of roots myself
# Eg, all have odd # of digits, built of 0 or 1, and 2 only in the ends or middle
def build_cache():
	mapp2 = set([1,4,9])
	for num_dig in range(1,2):
		print(num_dig)
		ranger = [set([0,1,2])]
		for i in range(0,num_dig):
			if( i == num_dig - 1 ):
				ranger.append(set([1,2]))
			else:
				ranger.append(set([0,1]))
		outs = []
		build_num(ranger,"",outs)
		for out in outs:
			trial_num = out + out[-2::-1]
			if( check_trial(trial_num) ):
				mapp2.add(int(trial_num)**2)
			trial_num = out[0:-1] + out[-2::-1]
			if( check_trial(trial_num) ):
				mapp2.add(int(trial_num)**2)
	print(len(mapp2))
	print(max(mapp2))
	print(len(str(max(mapp2))))
	l_cache = list(mapp2)
	l_cache.sort()
	f_cache = open('large_cache1.txt','w')
	for st in l_cache:
		f_cache.write( str(st) + "\n" )
	f_cache.close

# This line builds the cache above, which we write to a file.
# This takes about 40 mins to run, but I asked the contest staff if it's okay to persist and read back, and they confirmed.
#build_cache()

#If we have the cache, read it back first
f_cache = open('large_cache.txt','r')
mapp = set()
for i in range(0,46228):
	p=f_cache.readline()
	mapp.add(int(p))
f_cache.close
print( 'read map :', len(mapp))

base = "C-large-2"
f = open(base+'.in','r')
fout = open(base+'.out','w')

num = int(f.readline())
for case in range(1,num+1):
	prefix = "Case #" + str(case) + ": "
	l = f.readline()
	a,b = l.split()
	a = int(a)
	b = int(b)
	count = 0
	for sq in mapp:
		if( sq >= a and sq <= b ):
			count += 1
	fout.write( prefix + str(count) + "\n")

f.close
fout.close