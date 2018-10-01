import math

def getPair(N, K):
	# Z = [0 for i in xrange(N*2)];
	# Z[0] = N;	
	# for i in xrange(len(Z)/2):
	# 	if Z[i]%2==1:
	# 		Z[2*i + 1] = Z[2*i + 2] = Z[i]/2;
	# 	else:
	# 		if Z[i] != 0:
	# 			Z[2*i + 1] = Z[i]/2 -1;
	# 			Z[2*i + 2] = Z[i]/2;
	# 		else:
	# 			Z[2*i + 1] = 0;
	# 			Z[2*i + 2] = 0;
	Z = [];
	Z.append(N);
	for i in xrange(N/2):
		if Z[i]%2:
			Z.append(Z[i]/2);
			Z.append(Z[i]/2);
		else:
			Z.append(Z[i]/2-1);
			Z.append(Z[i]/2);

	level = math.log(K, 2);
	temp = math.floor(level);
	cnt = int(2 ** temp);
	work = Z[cnt-1 :2*(cnt-1) + 1]
	work = sorted(work, reverse=True);
	return work[int(K)-cnt];
	# print Z;
	# if K > N/2:
	# 	return (0, 0);

 		#  	power = int(math.log (K, 2) + 0.5)
 	# #    return base ** power == num

	# level = math.log(K, 2);
	# temp = math.floor(level);
	# cnt = 2 ** temp;
	# if level - temp <= 0.5:
	# 	i = Z.index(max(Z[int(cnt-1):2*int(cnt-1) + 1]));
	# 	return (Z[2*i+1], Z[2*i+2]);
	# else:
	# 	i = Z.index(min(Z[int(cnt-1):2*int(cnt-1) + 1]));
	# 	return (Z[2*i+1], Z[2*i+2]);



T = int(raw_input());
for i in xrange(T):
	arr = map(int, raw_input().split(" "));
	N = arr[0];
	K = float(arr[1]);
	ans = getPair(N, K);
	if ans == 0 or ans == 1:
		print "Case #%d: %d %d" % (i+1, 0, 0);
	elif ans%2:
		print "Case #%d: %d %d" % (i+1, ans/2, ans/2);
	else:
		print "Case #%d: %d %d" % (i+1, ans/2, ans/2-1);