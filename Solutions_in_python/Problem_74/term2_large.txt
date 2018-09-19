Python 2.7.1+ (r271:86832, Apr 11 2011, 18:13:53) 
[GCC 4.5.2] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> 50 ^ 10
56
>>> def prelimcheck(lst):
	i = 0
	for j in lst:
		i ^= j
	return i == 0

>>> prelimcheck([1 2 3 4 5])
SyntaxError: invalid syntax
>>> prelimcheck([1,2,3,4,5])
False
>>> prelimcheck([3,5,6])
True
>>> def get_subsets(lst,curr):
	if len(lst) == 0:
		return curr
	else:
		return get_subsets(lst[1:], cur + [i + [lst[0]] for i in curr])

	
>>> get_subsets(range(4))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    get_subsets(range(4))
TypeError: get_subsets() takes exactly 2 arguments (1 given)
>>> get_subsets(range(4),[])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    get_subsets(range(4),[])
  File "<pyshell#15>", line 5, in get_subsets
    return get_subsets(lst[1:], cur + [i + [lst[0]] for i in curr])
NameError: global name 'cur' is not defined
>>> def get_subsets(lst,curr):
	if len(lst) == 0:
		return curr
	else:
		return get_subsets(lst[1:], curr + [i + [lst[0]] for i in curr])

	
>>> get_subsets(range(4))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    get_subsets(range(4))
TypeError: get_subsets() takes exactly 2 arguments (1 given)
>>> get_subsets(range(4),[])
[]
>>> get_subsets(range(4),[[]])
[[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2], [3], [0, 3], [1, 3], [0, 1, 3], [2, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2, 3]]
>>> len(get_subsets(range(4),[[]]))
16
>>> len(get_subsets(range(5),[[]]))
32
>>> len(get_subsets(range(15),[[]]))
32768
>>> def get_subsets2(lst,curr):
	if len(lst) == 0:
		return curr
	else:
		return get_subsets(lst[1:], curr + [i + [lst[0]] for i in curr])

	
>>> def get_subsets2(lst):
	sl = set(lst)
	s = [set(i) for i in get_subsets(lst,[[]])]
	return zip(s,[sl - i for i in s])

>>> get_subsets2(range(3))
[(set([]), set([0, 1, 2])), (set([0]), set([1, 2])), (set([1]), set([0, 2])), (set([0, 1]), set([2])), (set([2]), set([0, 1])), (set([0, 2]), set([1])), (set([1, 2]), set([0])), (set([0, 1, 2]), set([]))]
>>> get_subsets2(range(3))[1]
(set([0]), set([1, 2]))
>>> get_subsets2(range(3))[5]
(set([0, 2]), set([1]))
>>> q = get_subsets2(range(16))
>>> def get_soln(lst)
SyntaxError: invalid syntax
>>> def get_soln(lst):
	s = get_subsets2(lst)
	s.sort(key = lambda x: sum(x[0]))
	for (a,b) in s:
		if not a or not b:
			continue
		if prelim_check(a) == prelim_check(b):
			return b

		
>>> get_soln([3,5,6])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    get_soln([3,5,6])
  File "<pyshell#44>", line 7, in get_soln
    if prelim_check(a) == prelim_check(b):
NameError: global name 'prelim_check' is not defined
>>> prelim_check = prelimcheck
>>> get_soln([3,5,6])
set([5, 6])
>>> def get_soln(lst):
	if not prelim_check(lst):
		return False
	s = get_subsets2(lst)
	s.sort(key = lambda x: sum(x[0]))
	for (a,b) in s:
		if not a or not b:
			continue
		if prelim_check(a) == prelim_check(b):
			return b
	return False

>>> get_soln([3,5,6])
set([5, 6])
>>> get_soln(range(1,16))
set([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
>>> get_soln(range(1,6))
False
>>> def dostuff(x):
	x = x.split('\n')[2:]
	x = x[::2]
	print x

	
>>> dostuff("""2
5
1 2 3 4 5
3
3 5 6""")
['1 2 3 4 5', '3 5 6']
>>> def dostuff(x):
	x = x.split('\n')[2:]
	x = x[::2]
	n = 0
	s = ""
	for i in x:
		n += 1
		q = get_soln(map(int,i.split(' ')))
		s += "Case #%d: %s" % (n,'NO' if q == False else str(q))
	print s

	
>>> dostuff("""2
5
1 2 3 4 5
3
3 5 6""")
Case #1: NOCase #2: set([5, 6])
>>> def dostuff(x):
	x = x.split('\n')[2:]
	x = x[::2]
	n = 0
	s = ""
	for i in x:
		n += 1
		q = get_soln(map(int,i.split(' ')))
		s += "Case #%d: %s\n" % (n,'NO' if q == False else str(q))
	print s

	
>>> dostuff("""2
5
1 2 3 4 5
3
3 5 6""")
Case #1: NO
Case #2: set([5, 6])

>>> 
>>> def dostuff(x):
	x = x.split('\n')[2:]
	x = x[::2]
	n = 0
	s = ""
	for i in x:
		n += 1
		q = get_soln(map(int,i.split(' ')))
		s += "Case #%d: %s\n" % (n,'NO' if q == False else str(sum(q)))
	print s

	
>>> dostuff("""2
5
1 2 3 4 5
3
3 5 6""")
Case #1: NO
Case #2: 11

>>> dostuff("""100
5
1 2 3 4 5
3
3 5 6
2
5 6
2
5 5
15
34407 249430 432624 727977 503220 946199 132164 715198 329249 294752 988260 130208 893869 109855 812294
15
899743 38791 739420 274195 463151 860700 189257 166098 639905 655455 378958 515950 198287 587678 558917
6
652205 534046 959623 293349 47598 766271
15
947365 242624 18143 482498 37206 690852 51106 377824 302511 845071 859696 507571 436112 716892 740839
6
699496 48031 60108 82233 519971 725723
15
787858 114427 878450 687375 926821 294336 571412 425913 882166 564423 781667 706193 611547 600425 688237
3
623122 366032 987801
11
471106 658903 697970 18946 331763 664758 276767 406132 404896 75917 658795
4
252708 419804 526722 898426
14
297005 640801 486831 581362 343854 803886 116636 414276 937877 788682 77112 442983 713989 221068
9
2273 1675 5974 240 1771 5452 9718 4885 15496
10
1552 9783 1960 5850 9018 1045 7725 5841 4431 4041
9
2726 4154 1661 981 28 1534 5299 1551 2154
12
8170 6356 3834 4994 1017 9222 2122 7880 5792 6846 5318 591
8
5044 6258 4493 4361 585 3124 6992 7791
9
5270 3375 1386 8751 7543 5336 7128 4247 15388
15
7126 8259 266 9472 8257 2046 5365 7471 2087 6585 5511 8234 9572 5121 9388
2
9632 1871
8
3110 5659 3411 8481 7383 9319 6619 5924
10
9338 2915 1082 933 3243 7090 3163 1882 7363 10333
8
376 5320 2188 9021 7969 8995 6008 4370
3
8331 2317 10630
13
1911 8270 2048 7944 3655 8093 3314 244 5295 8147 3463 2480 8870
6
7122 8608 4212 2125 9439 1684
13
6028 4555 3902 636 1972 5490 828 1702 9927 2752 8374 3352 7664
11
4581 1650 634 160 6950 2430 3991 6314 1813 6930 3119
6
1804 4811 5980 2821 6088 7112
15
9166 9351 612 5947 3695 6026 6527 2873 4991 1895 1464 2246 7161 8207 15141
10
8336 7173 7638 2813 8359 2536 1350 1151 8203 9155
3
5721 5175 622
9
7834 3273 5227 2951 9932 6618 7055 3120 9494
12
5939 4942 7883 5362 7717 7648 235 7343 3143 7349 9215 8904
8
4102 1611 4994 9958 2625 3549 6620 15721
5
4608 394 793 4673 1281
6
7983 9834 4707 8047 7853 10980
14
5877 3381 1688 4308 6041 5049 4088 6415 6755 8572 8353 737 8719 9227
3
9873 3167 10958
14
2972 2349 6473 2446 9713 4767 2748 626 9168 9855 3274 1803 447 8711
6
1761 1351 1762 846 2436 3982
3
8270 2543 10657
8
1113 7422 6569 7423 3911 5676 3875 3001
5
3128 6757 7596 2905 168
9
2551 7106 7934 9886 2111 5868 4856 4307 2486
12
346 9430 7387 4672 2969 5917 3177 8600 5768 3852 6899 6421
3
4730 9426 13992
11
7234 7844 2812 9265 9348 9048 9689 5149 5432 4849 9236
3
8678 93 8635
3
2352 9342 7914
8
3735 5052 9406 5589 3909 1233 4554 13854
11
6822 678 4179 3390 561 813 5514 7083 1690 248 3122
4
6016 5237 839 7763
12
6310 9327 3361 35 3870 4377 8539 4846 9072 4258 3992 1602
13
8170 6184 9070 1262 2640 5257 8431 7880 8644 1709 6612 61 15932
3
3881 4157 7956
7
4030 627 8930 1078 5323 9025 7315
12
9017 445 214 8526 6867 3113 4841 4479 6790 455 8803 2104
15
9023 6731 1889 732 2907 229 9985 4398 6018 9241 2809 2555 1741 518 13578
8
8484 7248 9772 5488 4623 8234 5658 6473
11
5441 2579 5755 3084 4801 9564 5172 6235 4873 9662 2222
5
7496 6379 7396 3946 5677
11
7807 6603 3500 1541 7158 3576 4764 2928 5923 8847 13907
3
2650 4631 6221
12
2223 8347 1351 8226 6329 9669 1482 152 6490 8708 6963 5394
8
7541 6332 3243 1959 2443 190 2965 3173
15
8080 3687 3191 2266 7157 379 8272 1461 3901 7515 6015 3377 3112 979 11746
3
6960 5759 3407
8
9883 5932 5413 8462 6630 7138 3431 6941
3
9826 5489 8231
8
1306 5807 7548 886 7142 7095 8653 11299
14
5491 2815 6036 8303 5568 2919 464 1755 5834 9178 8693 3261 878 8705
8
4055 6970 1441 8721 5540 6524 9343 7162
15
24 7499 6590 6258 8017 6464 8434 2524 9701 5241 535 8365 8369 4421 4466
13
1179 4557 4032 8561 6655 1756 8841 2734 841 973 2119 5451 4459
6
9008 9551 2173 4139 8089 3811
15
7623 6356 5021 4480 1847 4864 2704 8609 1190 6261 5019 2890 1873 9295 6976
7
932 3437 564 5224 2852 6031 1086
3
3906 4148 8054
9
9759 9173 1525 7128 4394 4837 4160 6604 4516
13
7702 2646 8030 2198 8993 9215 3645 3908 7050 2613 757 1588 5969
3
3308 6597 5417
10
4489 9691 8238 65 8114 5256 848 7013 5328 5090
8
1576 8358 6963 1895 4460 1078 6226 14290
12
2784 320 7089 4942 3758 6450 1640 8820 804 7926 6880 14317
10
5785 866 9638 2668 534 6754 1194 1988 6075 13968
11
981 9914 2572 2850 9145 2760 5799 9307 5189 1049 12176
11
2407 9739 4694 1765 7276 6394 6320 9164 5757 7564 4036
15
6489 6043 9025 8054 1039 4232 1196 811 6610 9039 3656 6177 1678 3862 1177
8
1593 9951 6169 5610 552 464 1415 4149
6
1256 1041 6299 5080 4625 7613
14
2046 1928 7371 7412 8453 2711 1830 8962 1489 4873 8922 9645 3768 6666
7
1526 9943 290 1053 3170 2851 8543
4
3199 8445 1014 12148
7
6336 8196 8873 7327 1699 4774 4855
11
3951 4258 9355 3463 9111 6179 6288 1216 1481 7295 2195
3
4179 2910 6925
4
1846 3436 8303 10805""")
Case #1: NO
Case #2: 11
Case #3: NO
Case #4: NO
Case #5: 7265299
Case #6: NO
Case #7: 3205494
Case #8: NO
Case #9: NO
Case #10: 9406823
Case #11: NO
Case #12: NO
Case #13: 1844952
Case #14: 6789250
Case #15: 47244
Case #16: 50201
Case #17: 20060
Case #18: NO
Case #19: 38063
Case #20: 57038
Case #21: 94494
Case #22: NO
Case #23: 46796
Case #24: 46409
Case #25: NO
Case #26: 18961
Case #27: 63490
Case #28: 31506
Case #29: 56546
Case #30: 38412
Case #31: NO
Case #32: 84690
Case #33: 55563
Case #34: 10896
Case #35: 52553
Case #36: 75445
Case #37: 47569
Case #38: NO
Case #39: 44697
Case #40: 78473
Case #41: 20831
Case #42: 64905
Case #43: 11292
Case #44: 18927
Case #45: 37877
Case #46: 20386
Case #47: NO
Case #48: 65092
Case #49: 23418
Case #50: NO
Case #51: 17313
Case #52: NO
Case #53: 46099
Case #54: 33852
Case #55: NO
Case #56: NO
Case #57: 81791
Case #58: 12113
Case #59: 35701
Case #60: NO
Case #61: 72125
Case #62: NO
Case #63: NO
Case #64: 26948
Case #65: 65013
Case #66: 10852
Case #67: 65182
Case #68: 27656
Case #69: 70759
Case #70: 12719
Case #71: NO
Case #72: NO
Case #73: 48850
Case #74: NO
Case #75: 48315
Case #76: 86884
Case #77: 51317
Case #78: NO
Case #79: NO
Case #80: 19562
Case #81: 12202
Case #82: 50571
Case #83: 63557
Case #84: 12014
Case #85: 54067
Case #86: 43768
Case #87: 65410
Case #88: 48936
Case #89: 60761
Case #90: 63351
Case #91: 68277
Case #92: NO
Case #93: NO
Case #94: NO
Case #95: 27086
Case #96: 23792
Case #97: 40361
Case #98: 53576
Case #99: 11104
Case #100: 22544

>>> 

>>> dostuff([5,5])
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    dostuff([5,5])
  File "<pyshell#73>", line 2, in dostuff
    x = x.split('\n')[2:]
AttributeError: 'list' object has no attribute 'split'
>>> get_soln([5,5])
False
>>> get_subsets([5,5],[[]])
[[], [5], [5], [5, 5]]
>>> 
>>> def get_soln(lst):
	if not prelim_check(lst):
		return False
	s = get_subsets2(lst)
	s.sort(key = lambda x: sum(x[0]))
	for (a,b) in s:
		if not a or not b:
			continue
		if prelim_check(a) == prelim_check(b):
			return b
	return False

>>> prelim_check([5,5])
True
>>> s = get_subsets2([5,5])
>>> s.sort(key = lambda x: sum(x[0]))
>>> for (a,b) in s:
		if not a or not b:
			continue
		if prelim_check(a) == prelim_check(b):
			print b

			
>>> s
[(set([]), set([5])), (set([5]), set([])), (set([5]), set([])), (set([5]), set([]))]
>>> def get_complement(s,spacedict):
	for i in s:
		spacedict[i] -= 1
	out = []
	for i in spacedict:
		out += [i]*spacedict[i]
	return out

>>> def get_subsets2(lst,spacedict):
	s = [get_complement(i) for i in lst]
	return zip(lst,s)

>>> def get_subsets2(lst,spacedict):
	s = [get_complement(i,spacedict) for i in get_subsets(lst,[])]
	return zip(lst,s)

>>> spacedict = dict([(i,1) for i in range(1,6)])
>>> spacedict
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
>>> def get_subsets2(lst,spacedict):
	s = [get_complement(i,spacedict) for i in get_subsets(lst,[])]
	return zip(lst,s)

>>> get_subsets2(range(1,6),spacedict)
[]
>>> def get_subsets2(lst,spacedict):
	s = [get_complement(i,spacedict) for i in get_subsets(lst,[[]])]
	return zip(lst,s)

>>> get_subsets2(range(1,6),spacedict)
[(1, [1, 2, 3, 4, 5]), (2, [2, 3, 4, 5]), (3, [3, 4, 5]), (4, [3, 4, 5]), (5, [4, 5])]
>>> def get_subsets2(lst,spacedict):
	ss = get_subsets(lst,[[]])
	s = [get_complement(i,spacedict) for i in ss]
	return zip(ss,s)

>>> get_subsets2(range(1,6),spacedict)
[([], []), ([1], []), ([2], []), ([1, 2], []), ([3], []), ([1, 3], []), ([2, 3], []), ([1, 2, 3], []), ([4], []), ([1, 4], []), ([2, 4], []), ([1, 2, 4], []), ([3, 4], []), ([1, 3, 4], []), ([2, 3, 4], []), ([1, 2, 3, 4], []), ([5], []), ([1, 5], []), ([2, 5], []), ([1, 2, 5], []), ([3, 5], []), ([1, 3, 5], []), ([2, 3, 5], []), ([1, 2, 3, 5], []), ([4, 5], []), ([1, 4, 5], []), ([2, 4, 5], []), ([1, 2, 4, 5], []), ([3, 4, 5], []), ([1, 3, 4, 5], []), ([2, 3, 4, 5], []), ([1, 2, 3, 4, 5], [])]
>>> 
>>> get_complement([1,2,3],spacedict)
[]
>>> print spacedict
{1: -32, 2: -32, 3: -32, 4: -31, 5: -31}
>>> def get_complement(s,spacedict):
	sd = spacedict.copy()
	for i in s:
		spacedict[i] -= 1
	out = []
	for i in spacedict:
		out += [i]*spacedict[i]
	return out

>>> spacedict = dict([(i,1) for i in range(1,6)])
>>> def get_complement(s,spacedict):
	sd = spacedict.copy()
	for i in s:
		spacedict[i] -= 1
	out = []
	for i in spacedict:
		out += [i]*spacedict[i]
	return out

>>> get_complement([1,2,3],spacedict)
[4, 5]
>>> def get_complement(s,spacedict):
	sd = spacedict.copy()
	for i in s:
		sd[i] -= 1
	out = []
	for i in sd:
		out += [i]*sd[i]
	return out

>>> get_complement([1,2,3],spacedict)
[4, 5]
>>> spacedict = dict([(i,1) for i in range(1,6)])
>>> get_complement([1,2,3],spacedict)
[4, 5]
>>> get_subsets2(range(1,6),spacedict)
[([], [1, 2, 3, 4, 5]), ([1], [2, 3, 4, 5]), ([2], [1, 3, 4, 5]), ([1, 2], [3, 4, 5]), ([3], [1, 2, 4, 5]), ([1, 3], [2, 4, 5]), ([2, 3], [1, 4, 5]), ([1, 2, 3], [4, 5]), ([4], [1, 2, 3, 5]), ([1, 4], [2, 3, 5]), ([2, 4], [1, 3, 5]), ([1, 2, 4], [3, 5]), ([3, 4], [1, 2, 5]), ([1, 3, 4], [2, 5]), ([2, 3, 4], [1, 5]), ([1, 2, 3, 4], [5]), ([5], [1, 2, 3, 4]), ([1, 5], [2, 3, 4]), ([2, 5], [1, 3, 4]), ([1, 2, 5], [3, 4]), ([3, 5], [1, 2, 4]), ([1, 3, 5], [2, 4]), ([2, 3, 5], [1, 4]), ([1, 2, 3, 5], [4]), ([4, 5], [1, 2, 3]), ([1, 4, 5], [2, 3]), ([2, 4, 5], [1, 3]), ([1, 2, 4, 5], [3]), ([3, 4, 5], [1, 2]), ([1, 3, 4, 5], [2]), ([2, 3, 4, 5], [1]), ([1, 2, 3, 4, 5], [])]
>>> get_subsets2([5,5],spacedict)
[([], [1, 2, 3, 4, 5]), ([5], [1, 2, 3, 4]), ([5], [1, 2, 3, 4]), ([5, 5], [1, 2, 3, 4])]
>>> spacedict = {5: 2}
>>> get_subsets2([5,5],spacedict)
[([], [5, 5]), ([5], [5]), ([5], [5]), ([5, 5], [])]
>>> def get_soln(lst):
	if not prelim_check(lst):
		return False
	sd = {}
	for i in lst:
		if i in sd:
			sd[i] += 1
		else:
			sd[i] = 1
	s = get_subsets2(lst,sd)
	s.sort(key = lambda x: sum(x[0]))
	for (a,b) in s:
		if not a or not b:
			continue
		if prelim_check(a) == prelim_check(b):
			return b
	return False

>>> get_soln([5,5])
[5]
>>> get_soln([3,5,6])
[5, 6]
>>> 
>>> def dostuff(x):
	x = x.split('\n')[2:]
	x = x[::2]
	n = 0
	s = ""
	for i in x:
		n += 1
		q = get_soln(map(int,i.split(' ')))
		s += "Case #%d: %s\n" % (n,'NO' if q == False else str(sum(q)))
	print s

	
>>> dostuff("""100
5
1 2 3 4 5
3
3 5 6
2
5 6
2
5 5
15
34407 249430 432624 727977 503220 946199 132164 715198 329249 294752 988260 130208 893869 109855 812294
15
899743 38791 739420 274195 463151 860700 189257 166098 639905 655455 378958 515950 198287 587678 558917
6
652205 534046 959623 293349 47598 766271
15
947365 242624 18143 482498 37206 690852 51106 377824 302511 845071 859696 507571 436112 716892 740839
6
699496 48031 60108 82233 519971 725723
15
787858 114427 878450 687375 926821 294336 571412 425913 882166 564423 781667 706193 611547 600425 688237
3
623122 366032 987801
11
471106 658903 697970 18946 331763 664758 276767 406132 404896 75917 658795
4
252708 419804 526722 898426
14
297005 640801 486831 581362 343854 803886 116636 414276 937877 788682 77112 442983 713989 221068
9
2273 1675 5974 240 1771 5452 9718 4885 15496
10
1552 9783 1960 5850 9018 1045 7725 5841 4431 4041
9
2726 4154 1661 981 28 1534 5299 1551 2154
12
8170 6356 3834 4994 1017 9222 2122 7880 5792 6846 5318 591
8
5044 6258 4493 4361 585 3124 6992 7791
9
5270 3375 1386 8751 7543 5336 7128 4247 15388
15
7126 8259 266 9472 8257 2046 5365 7471 2087 6585 5511 8234 9572 5121 9388
2
9632 1871
8
3110 5659 3411 8481 7383 9319 6619 5924
10
9338 2915 1082 933 3243 7090 3163 1882 7363 10333
8
376 5320 2188 9021 7969 8995 6008 4370
3
8331 2317 10630
13
1911 8270 2048 7944 3655 8093 3314 244 5295 8147 3463 2480 8870
6
7122 8608 4212 2125 9439 1684
13
6028 4555 3902 636 1972 5490 828 1702 9927 2752 8374 3352 7664
11
4581 1650 634 160 6950 2430 3991 6314 1813 6930 3119
6
1804 4811 5980 2821 6088 7112
15
9166 9351 612 5947 3695 6026 6527 2873 4991 1895 1464 2246 7161 8207 15141
10
8336 7173 7638 2813 8359 2536 1350 1151 8203 9155
3
5721 5175 622
9
7834 3273 5227 2951 9932 6618 7055 3120 9494
12
5939 4942 7883 5362 7717 7648 235 7343 3143 7349 9215 8904
8
4102 1611 4994 9958 2625 3549 6620 15721
5
4608 394 793 4673 1281
6
7983 9834 4707 8047 7853 10980
14
5877 3381 1688 4308 6041 5049 4088 6415 6755 8572 8353 737 8719 9227
3
9873 3167 10958
14
2972 2349 6473 2446 9713 4767 2748 626 9168 9855 3274 1803 447 8711
6
1761 1351 1762 846 2436 3982
3
8270 2543 10657
8
1113 7422 6569 7423 3911 5676 3875 3001
5
3128 6757 7596 2905 168
9
2551 7106 7934 9886 2111 5868 4856 4307 2486
12
346 9430 7387 4672 2969 5917 3177 8600 5768 3852 6899 6421
3
4730 9426 13992
11
7234 7844 2812 9265 9348 9048 9689 5149 5432 4849 9236
3
8678 93 8635
3
2352 9342 7914
8
3735 5052 9406 5589 3909 1233 4554 13854
11
6822 678 4179 3390 561 813 5514 7083 1690 248 3122
4
6016 5237 839 7763
12
6310 9327 3361 35 3870 4377 8539 4846 9072 4258 3992 1602
13
8170 6184 9070 1262 2640 5257 8431 7880 8644 1709 6612 61 15932
3
3881 4157 7956
7
4030 627 8930 1078 5323 9025 7315
12
9017 445 214 8526 6867 3113 4841 4479 6790 455 8803 2104
15
9023 6731 1889 732 2907 229 9985 4398 6018 9241 2809 2555 1741 518 13578
8
8484 7248 9772 5488 4623 8234 5658 6473
11
5441 2579 5755 3084 4801 9564 5172 6235 4873 9662 2222
5
7496 6379 7396 3946 5677
11
7807 6603 3500 1541 7158 3576 4764 2928 5923 8847 13907
3
2650 4631 6221
12
2223 8347 1351 8226 6329 9669 1482 152 6490 8708 6963 5394
8
7541 6332 3243 1959 2443 190 2965 3173
15
8080 3687 3191 2266 7157 379 8272 1461 3901 7515 6015 3377 3112 979 11746
3
6960 5759 3407
8
9883 5932 5413 8462 6630 7138 3431 6941
3
9826 5489 8231
8
1306 5807 7548 886 7142 7095 8653 11299
14
5491 2815 6036 8303 5568 2919 464 1755 5834 9178 8693 3261 878 8705
8
4055 6970 1441 8721 5540 6524 9343 7162
15
24 7499 6590 6258 8017 6464 8434 2524 9701 5241 535 8365 8369 4421 4466
13
1179 4557 4032 8561 6655 1756 8841 2734 841 973 2119 5451 4459
6
9008 9551 2173 4139 8089 3811
15
7623 6356 5021 4480 1847 4864 2704 8609 1190 6261 5019 2890 1873 9295 6976
7
932 3437 564 5224 2852 6031 1086
3
3906 4148 8054
9
9759 9173 1525 7128 4394 4837 4160 6604 4516
13
7702 2646 8030 2198 8993 9215 3645 3908 7050 2613 757 1588 5969
3
3308 6597 5417
10
4489 9691 8238 65 8114 5256 848 7013 5328 5090
8
1576 8358 6963 1895 4460 1078 6226 14290
12
2784 320 7089 4942 3758 6450 1640 8820 804 7926 6880 14317
10
5785 866 9638 2668 534 6754 1194 1988 6075 13968
11
981 9914 2572 2850 9145 2760 5799 9307 5189 1049 12176
11
2407 9739 4694 1765 7276 6394 6320 9164 5757 7564 4036
15
6489 6043 9025 8054 1039 4232 1196 811 6610 9039 3656 6177 1678 3862 1177
8
1593 9951 6169 5610 552 464 1415 4149
6
1256 1041 6299 5080 4625 7613
14
2046 1928 7371 7412 8453 2711 1830 8962 1489 4873 8922 9645 3768 6666
7
1526 9943 290 1053 3170 2851 8543
4
3199 8445 1014 12148
7
6336 8196 8873 7327 1699 4774 4855
11
3951 4258 9355 3463 9111 6179 6288 1216 1481 7295 2195
3
4179 2910 6925
4
1846 3436 8303 10805""")
Case #1: NO
Case #2: 11
Case #3: NO
Case #4: 5
Case #5: 7265299
Case #6: NO
Case #7: 3205494
Case #8: NO
Case #9: NO
Case #10: 9406823
Case #11: NO
Case #12: NO
Case #13: 1844952
Case #14: 6789250
Case #15: 47244
Case #16: 50201
Case #17: 20060
Case #18: NO
Case #19: 38063
Case #20: 57038
Case #21: 94494
Case #22: NO
Case #23: 46796
Case #24: 46409
Case #25: NO
Case #26: 18961
Case #27: 63490
Case #28: 31506
Case #29: 56546
Case #30: 38412
Case #31: NO
Case #32: 84690
Case #33: 55563
Case #34: 10896
Case #35: 52553
Case #36: 75445
Case #37: 47569
Case #38: NO
Case #39: 44697
Case #40: 78473
Case #41: 20831
Case #42: 64905
Case #43: 11292
Case #44: 18927
Case #45: 37877
Case #46: 20386
Case #47: NO
Case #48: 65092
Case #49: 23418
Case #50: NO
Case #51: 17313
Case #52: NO
Case #53: 46099
Case #54: 33852
Case #55: NO
Case #56: NO
Case #57: 81791
Case #58: 12113
Case #59: 35701
Case #60: NO
Case #61: 72125
Case #62: NO
Case #63: NO
Case #64: 26948
Case #65: 65013
Case #66: 10852
Case #67: 65182
Case #68: 27656
Case #69: 70759
Case #70: 12719
Case #71: NO
Case #72: NO
Case #73: 48850
Case #74: NO
Case #75: 48315
Case #76: 86884
Case #77: 51317
Case #78: NO
Case #79: NO
Case #80: 19562
Case #81: 12202
Case #82: 50571
Case #83: 63557
Case #84: 12014
Case #85: 54067
Case #86: 43768
Case #87: 65410
Case #88: 48936
Case #89: 60761
Case #90: 63351
Case #91: 68277
Case #92: NO
Case #93: NO
Case #94: NO
Case #95: 27086
Case #96: 23792
Case #97: 40361
Case #98: 53576
Case #99: 11104
Case #100: 22544

>>> dostuff("""100
5
1 2 3 4 5
3
3 5 6
2
5 6
2
5 5
15
844422 757955 420572 258917 511275 404935 783799 303313 476597 583383 908113 504687 281838 755805 414105
15
618369 250507 909747 982786 810218 902166 310148 729832 898839 683984 472143 100702 434172 610887 913012
8
865310 260493 805028 548700 14042 719705 398824 824845
3
493578 867603 701721
6
870472 191068 567511 238616 967541 683438
8
80446 320055 507941 932834 109058 551268 706562 547441
9
963839 603186 587618 444990 596287 384902 575652 290330 189392
10
656660 476531 89825 757604 876771 923382 842461 898174 923083 760991
7
705284 275635 811629 849486 895039 589802 734273
10
450564 660246 996258 916942 793326 82373 612784 486445 630148 845078
12
1172 2205 7946 3326 8160 1007 1464 6977 453 5739 9101 10536
11
267 6350 6064 5760 3913 3702 9806 364 217 9611 7098
3
2106 8008 6002
2
4257 1016
5
6470 3503 1804 5037 72
3
9883 1994 8529
12
8384 9185 1695 6727 9666 581 6763 8455 3424 2507 5968 4329
4
4717 4100 5692 5205
6
3572 8377 2510 5607 125 12569
6
457 2809 2402 9532 3523 2879
15
6338 6211 7157 3881 4145 6509 16 1924 3345 2395 6374 3787 8755 5682 15603
7
7019 4183 6622 468 4454 2593 2161
9
4873 5615 7555 8839 4946 3121 4669 8091 11047
13
1881 9995 6331 835 7256 9869 4019 6786 3162 2136 7174 24 8228
3
1190 6493 7675
5
9786 1002 8540 3967 814
8
7924 8614 1335 5209 6508 3471 8719 6352
3
407 6810 6925
15
9385 9099 421 7492 7014 6554 7124 9028 6402 3725 5380 2079 5872 89 15762
6
7897 7185 3383 6206 413 5724
15
2896 3948 5485 2935 4781 2398 483 1796 5231 709 4032 3286 4148 995 345
8
8409 9763 3437 4791 6996 4266 3020 7348
14
6268 3756 9746 6389 659 847 7499 612 79 3939 5191 4486 4887 5849
7
3684 9885 2610 7772 4313 3586 8780
14
7021 9031 4517 6770 1190 3980 2073 422 9480 2159 1464 1980 3781 4302
4
9887 9830 1485 1332
11
8777 4955 9171 3225 4985 4987 6701 2020 6098 2188 7373
15
8991 8182 355 1484 2569 7842 8424 5830 7182 8071 664 847 8689 395 14567
3
153 8440 8289
4
1489 6561 9686 14758
14
5025 5739 6786 8052 7579 9906 7470 9058 2062 5355 5987 8257 4823 15433
7
5864 8514 7981 6570 3 1820 5069
3
8599 9430 1345
7
8101 623 6410 1274 2871 8300 11105
3
4179 4919 868
12
6736 1514 9868 4112 6118 3867 471 4709 1514 325 6175 6300
9
3467 3835 7765 4904 8813 6102 4672 6324 12610
3
6826 6221 743
3
9118 7994 9169
11
8103 5191 7855 1892 7822 4446 7567 4555 7896 754 447
8
9011 9448 6666 5718 2160 935 8194 8888
11
4202 3054 1135 4260 5661 9229 9358 4157 993 7739 7343
8
6865 302 9193 9623 7226 786 704 105
3
3479 100 3571
13
706 8935 2080 2048 6738 9383 1232 72 3692 247 6049 8592 1870
6
9592 1302 9666 3623 4734 6645
15
9582 6360 1841 9930 1026 5809 1565 8977 9457 8044 3159 2429 7549 2911 871
3
1323 206 1509
3
4203 5508 1519
3
4222 6370 846
7
9490 579 4087 4173 7282 3207 10270
6
4709 9503 7966 2770 5582 14200
13
4462 3988 7677 4318 2480 4535 9372 1426 4625 6374 4833 2037 13619
11
6188 78 2986 7687 6290 5453 1563 7063 4715 6782 5513
5
7620 2801 9841 1209 8838
5
5262 5817 3963 1021 3761
5
7553 9088 5955 355 10273
6
3399 5302 2491 9200 1636 4149
9
5740 6272 5314 4109 6346 4035 7786 7882 7562
7
6289 1571 6971 3815 5911 1396 6413
6
4727 4152 4768 6947 3183 1955
3
3002 7453 5799
10
256 4716 8886 102 5269 665 8672 6863 7420 99
3
412 6209 6621
14
6997 7271 2267 7517 2880 1055 4609 3302 1683 4218 8973 4353 4473 7089
3
9104 4442 13002
7
8069 3896 2202 1962 9401 5866 498
5
847 1868 570 6381 7892
10
6126 7050 5122 2845 8775 3531 4583 6319 5162 8597
15
9298 9341 5810 4903 7042 2155 2659 439 1629 39 6547 1405 7867 6806 9707
14
4538 3396 1024 8829 7948 3230 4558 3252 289 444 3688 2096 5246 9936
4
6727 7357 3123 2761
5
3440 7125 446 9342 724
12
475 8091 9789 4606 1182 815 988 7655 4141 9193 4407 4858
7
7549 8294 394 1804 4901 1281 11705
15
3196 4349 5571 2856 5411 2012 2967 4418 6047 5362 2610 2318 1188 7835 990
5
2846 7361 6597 7420 5153
3
6452 1183 7373
11
7035 6607 2216 8318 2402 5182 6747 2337 6286 2869 14335
13
5532 3279 5855 253 1299 3956 9758 5105 765 7651 7815 7749 12069
11
2135 7326 8162 7600 3535 5911 6290 9009 1081 8340 4941
7
4557 127 2201 6528 6609 4947 2601
8
3140 8478 2592 6044 7035 8217 7854 3841
3
7265 9617 14832
8
7258 6579 2602 6716 3050 3564 5396 1773
4
220 6279 246 450""")
Case #1: NO
Case #2: 11
Case #3: NO
Case #4: 5
Case #5: 7950799
Case #6: NO
Case #7: NO
Case #8: 1569324
Case #9: 3327578
Case #10: NO
Case #11: NO
Case #12: 7115657
Case #13: 4585513
Case #14: NO
Case #15: 57633
Case #16: 52935
Case #17: 14010
Case #18: NO
Case #19: 16814
Case #20: 18412
Case #21: 67103
Case #22: 15614
Case #23: 32635
Case #24: NO
Case #25: 82106
Case #26: 27032
Case #27: 55635
Case #28: NO
Case #29: 14168
Case #30: NO
Case #31: 46797
Case #32: 13735
Case #33: 95337
Case #34: 30395
Case #35: 43123
Case #36: NO
Case #37: NO
Case #38: 38020
Case #39: 57748
Case #40: 21202
Case #41: 58460
Case #42: 83737
Case #43: 16729
Case #44: 31005
Case #45: 99470
Case #46: NO
Case #47: 18029
Case #48: 38061
Case #49: 9098
Case #50: NO
Case #51: 55025
Case #52: 13047
Case #53: NO
Case #54: NO
Case #55: NO
Case #56: NO
Case #57: 34699
Case #58: 7050
Case #59: NO
Case #60: 34260
Case #61: 78639
Case #62: 2832
Case #63: 9711
Case #64: NO
Case #65: 38509
Case #66: 41960
Case #67: 68320
Case #68: 54240
Case #69: NO
Case #70: 18803
Case #71: 32869
Case #72: NO
Case #73: 51011
Case #74: 30970
Case #75: 23777
Case #76: 13252
Case #77: 42849
Case #78: 12830
Case #79: NO
Case #80: 22106
Case #81: NO
Case #82: 16988
Case #83: 55265
Case #84: NO
Case #85: 58185
Case #86: 17207
Case #87: NO
Case #88: 55725
Case #89: 35534
Case #90: NO
Case #91: NO
Case #92: NO
Case #93: 62118
Case #94: 70833
Case #95: 63249
Case #96: 27443
Case #97: NO
Case #98: 24449
Case #99: 35165
Case #100: NO

>>> 
>>> 
>>> def get_next_instruction(instructs,bot):
	if bot == 'O':
		for i in instructs:
			if i > 0:
				return i
	else:
		for i in instructs:
			if i < 0:
				return i
	else:
		
SyntaxError: invalid syntax
>>> def get_next_instruction(instructs,bot):
	if bot == 'O':
		for i in instructs:
			if i > 0:
				return i
		else:
			return False
	else:
		for i in instructs:
			if i < 0:
				return i
		else:
			return False

		
>>> get_next_instruction([],'o')
False
>>> get_next_instruction([],'O')
False
>>> def sign(x):
	if x > 0:
		return 1
	else:
		return -1

	
>>> def get_next_instruction(instructs,bot):
	n = 0
	if bot == 'O':
		for i in instructs:
			n += 1
			if i > 0:
				return (i,n)
		else:
			return False
	else:
		for i in instructs:
			n += 1
			if i < 0:
				return (i,n)
		else:
			return False

		
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction('O',instructs)
		b_inst,bt = get_next_instruction('B',instructs)
		b_inst = abs(b_inst)
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			o = o_inst
			time += abs(o_inst - o)
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			b = b_inst
			time += abs(b_inst - b)
		instructs = instructs[1:]
	return time

>>> def parse_text(t):
	t = t.replace('B ','-').split('\n')[1:]
	t = [map(int,i.split(' ')[1:]) for i in t]
	return t

>>> parse_text("""4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
Traceback (most recent call last):
  File "<pyshell#195>", line 3, in <module>
    2 B 2 B 1""")
  File "<pyshell#194>", line 3, in parse_text
    t = [map(int,i.split(' ')[1:]) for i in t]
ValueError: invalid literal for int() with base 10: 'O'
>>> def parse_text(t):
	t = t.replace('B ','-').replace('O ','').split('\n')[1:]
	t = [map(int,i.split(' ')[1:]) for i in t]
	return t

>>> parse_text("""4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
[[5, 8, -100], [-2, -1]]
>>> def parse_text(t):
	t = t.replace('B ','-').replace('O ','').split('\n')[1:]
	t = [map(int,i.split(' ')[1:]) for i in t]
	return t

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
[[2, -1, -2, 4], [5, 8, -100], [-2, -1]]
>>> solve_puzzle([2, -1, -2, 4])
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    solve_puzzle([2, -1, -2, 4])
  File "<pyshell#188>", line 6, in solve_puzzle
    o_inst,ot = get_next_instruction('O',instructs)
TypeError: 'bool' object is not iterable
>>> def get_next_instruction(instructs,bot):
	n = 0
	if bot == 'O':
		for i in instructs:
			n += 1
			if i > 0:
				return (i,n)
		else:
			return (False,999)
	else:
		for i in instructs:
			n += 1
			if i < 0:
				return (i,n)
		else:
			return (False,999)

		
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction('O',instructs)
		b_inst,bt = get_next_instruction('B',instructs)
		b_inst = abs(b_inst)
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			o = o_inst
			time += abs(o_inst - o)
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			b = b_inst
			time += abs(b_inst - b)
		instructs = instructs[1:]
	return timedef get_next_instruction(instructs,bot):
		n = 0
		if bot == 'O':
			for i in instructs:
				n += 1
				if i > 0:
					return (i,n)
			else:
				return (0,999)
		else:
			for i in instructs:
				n += 1
				if i < 0:
					return (i,n)
			else:
				return (0,999)
				
SyntaxError: invalid syntax
>>> def get_next_instruction(instructs,bot):
		n = 0
		if bot == 'O':
			for i in instructs:
				n += 1
				if i > 0:
					return (i,n)
			else:
				return (0,999)
		else:
			for i in instructs:
				n += 1
				if i < 0:
					return (i,n)
			else:
				return (0,999)

>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction('O',instructs)
		b_inst,bt = get_next_instruction('B',instructs)
		b_inst = abs(b_inst)
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			o = o_inst
			time += abs(o_inst - o)
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			b = b_inst
			time += abs(b_inst - b)
		instructs = instructs[1:]
	return time

>>> solve_puzzle([2, -1, -2, 4])
0
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			o = o_inst
			time += abs(o_inst - o)
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			b = b_inst
			time += abs(b_inst - b)
		instructs = instructs[1:]
	return time

>>> solve_puzzle([2, -1, -2, 4])
0
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, ot, b_inst, bt
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			o = o_inst
			time += abs(o_inst - o)
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			b = b_inst
			time += abs(b_inst - b)
		instructs = instructs[1:]
	return time

>>> solve_puzzle([2, -1, -2, 4])
2 1 1 2
4 3 1 1
4 2 2 1
4 1 0 999
0
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, ot, b_inst, bt
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			time += abs(o_inst - o)
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			time += abs(b_inst - b)
			b = b_inst
		instructs = instructs[1:]
	return time

>>> solve_puzzle([2, -1, -2, 4])
2 1 1 2
4 3 1 1
4 2 2 1
4 1 0 999
5
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, ot, b_inst, bt
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			time += min(1,abs(o_inst - o))
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			time += min(abs(b_inst - b),1)
			b = b_inst
		instructs = instructs[1:]
	return time

>>> solve_puzzle([2, -1, -2, 4])
2 1 1 2
4 3 1 1
4 2 2 1
4 1 0 999
3
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, ot, b_inst, bt
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) > abs(b_inst - b) else sign(b_inst - b)*abs(o_inst - o)
			time += max(1,abs(o_inst - o))
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) > abs(o_inst - o) else sign(o_inst - o)*abs(b_inst - b)
			time += max(abs(b_inst - b),1)
			b = b_inst
		instructs = instructs[1:]
	return time

>>> solve_puzzle([2, -1, -2, 4])
2 1 1 2
4 3 1 1
4 2 2 1
4 1 0 999
6
>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
[[2, -1, -2, 4], [5, 8, -100], [-2, -1]]
>>> def parse_text(t):
	t = t.replace('B ','-').replace('O ','').split('\n')[1:]
	t = [map(int,i.split(' ')[1:]) for i in t]
	print [solve_puzzle(i) for i in t]

	
>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
2 1 1 2
4 3 1 1
4 2 2 1
4 1 0 999
5 1 100 3
8 1 100 2
0 999 100 1
0 999 2 1
0 999 1 1
[6, 104, 2]
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, ot, b_inst, bt
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) >= abs(b_inst - b) else sign(b_inst - b)*(abs(o_inst - o)+1)
			time += abs(o_inst - o)+1
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) >= abs(o_inst - o) else sign(o_inst - o)*(abs(b_inst - b)+1)
			time += abs(b_inst - b)+1
			b = b_inst
		instructs = instructs[1:]
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
2 1 1 2
4 3 1 1
4 2 2 1
4 1 0 999
5 1 100 3
8 1 100 2
0 999 100 1
0 999 2 1
0 999 1 1
[8, 106, 4]
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, b_inst, t
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) >= abs(b_inst - b) else sign(b_inst - b)*(abs(o_inst - o)+1)
			time += abs(o_inst - o)+1
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) >= abs(o_inst - o) else sign(o_inst - o)*(abs(b_inst - b)+1)
			time += abs(b_inst - b)+1
			b = b_inst
		instructs = instructs[1:]
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
2 1
Traceback (most recent call last):
  File "<pyshell#234>", line 4, in <module>
    2 B 2 B 1""")
  File "<pyshell#227>", line 4, in parse_text
    print [solve_puzzle(i) for i in t]
  File "<pyshell#233>", line 9, in solve_puzzle
    print o_inst, b_inst, t
NameError: global name 't' is not defined
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, b_inst, time
		if bt == ot == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) >= abs(b_inst - b) else sign(b_inst - b)*(abs(o_inst - o)+1)
			time += abs(o_inst - o)+1
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) >= abs(o_inst - o) else sign(o_inst - o)*(abs(b_inst - b)+1)
			time += abs(b_inst - b)+1
			b = b_inst
		instructs = instructs[1:]
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
2 1 0
4 1 2
4 2 3
4 0 5
5 100 0
8 100 5
0 100 9
0 2 0
0 1 2
[8, 106, 4]
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o_inst, b_inst, time
		if b == o == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) >= abs(b_inst - b) else sign(b_inst - b)*(abs(o_inst - o)+1)
			time += abs(o_inst - o)+1
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) >= abs(o_inst - o) else sign(o_inst - o)*(abs(b_inst - b)+1)
			time += abs(b_inst - b)+1
			b = b_inst
		instructs = instructs[1:]
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
2 1 0
4 1 2
4 2 3
4 0 5
5 100 0
8 100 5
0 100 9
0 2 0
0 1 2
[8, 106, 4]
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o, b, time
		if b == o == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) >= abs(b_inst - b) else sign(b_inst - b)*(abs(o_inst - o)+1)
			time += abs(o_inst - o)+1
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) >= abs(o_inst - o) else sign(o_inst - o)*(abs(b_inst - b)+1)
			time += abs(b_inst - b)+1
			b = b_inst
		instructs = instructs[1:]
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1""")
1 1 0
2 1 2
1 1 3
2 2 5
1 1 0
5 5 5
8 4 9
1 1 0
0 2 2
[8, 106, 4]
>>> parse_text("""3
4 O 2 B 1 B 2 O 4
""")
1 1 0
2 1 2
1 1 3
2 2 5
[8, 0]
>>> 
>>> def solve_puzzle(instructs):
	time=0
	o = 1
	b = 1
	while instructs:
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		print o, b, time
		if b == o == 999:
			break
		if ot < bt:
			b = b_inst if abs(o_inst - o) >= abs(b_inst - b) else sign(b_inst - b)*(abs(o_inst - o)+1)
			time += abs(o_inst - o)+1
			o = o_inst
		else:
			o = o_inst if abs(b_inst - b) >= abs(o_inst - o) else sign(o_inst - o)*(abs(b_inst - b)+1)
			time += abs(b_inst - b)+1
			b = b_inst
		instructs = instructs[1:]
	return time

>>> def solve_puzzle(instructs):
	time = 0
	o = 1
	b = 1
	while 1:
		time += 1
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		if o_inst != o:
			o += sign(o_inst - o)
		else:
			if ot < bt:
				#simulate push
				o_inst, ot = get_next_instruction(instructs,'O')
		if b_inst != b:
			b += sign(b_inst - b)
		else:
			if bt < ot:
				b_inst, bt = get_next_instruction(instructs,'B')
				b_inst = abs(b_inst)
		if ot == bt == 999:
			break
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
""")
Traceback (most recent call last):
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1413, in __call__
    return self.func(*args)
  File "/usr/lib/python2.7/idlelib/MultiCall.py", line 167, in handler
    r = l[i](event)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1140, in enter_callback
    self.runit()
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1181, in runit
    more = self.interp.runsource(line)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 619, in runsource
    return InteractiveInterpreter.runsource(self, source, filename)
  File "/usr/lib/python2.7/code.py", line 87, in runsource
    self.runcode(code)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 755, in runcode
    self.showtraceback()
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 692, in showtraceback
    InteractiveInterpreter.showtraceback(self)
  File "/usr/lib/python2.7/code.py", line 162, in showtraceback
    map(self.write, list)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 765, in write
    self.tkconsole.stderr.write(s)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1246, in write
    self.shell.write(s, self.tags)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1235, in write
    raise KeyboardInterrupt
KeyboardInterrupt

def solve_puzzle(instructs):
	time = 0
	o = 1
	b = 1
	while 1:
		time += 1
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		if o_inst != o:
			o += sign(o_inst - o)
		else:
			if ot < bt:
				#simulate push
				o_inst, ot = get_next_instruction(instructs[1:],'O')
		if b_inst != b:
			b += sign(b_inst - b)
		else:
			if bt < ot:
				b_inst, bt = get_next_instruction(instructs[1:],'B')
				b_inst = abs(b_inst)
		if ot == bt == 999:
			break
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
""")
Traceback (most recent call last):
  File "<pyshell#268>", line 3, in <module>
    """)
  File "<pyshell#227>", line 4, in parse_text
    print [solve_puzzle(i) for i in t]
  File "<pyshell#267>", line 21, in solve_puzzle
    b_inst, bt = get_next_instruction(instructs[1:],'B')
KeyboardInterrupt
>>> def solve_puzzle(instructs):
	time = 0
	o = 1
	b = 1
	while 1:
		time += 1
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		pause = False
		if o_inst != o:
			o += sign(o_inst - o)
		else:
			if ot < bt:
				#simulate push
				o_inst, ot = get_next_instruction(instructs[1:],'O')
				pause = True
		if b_inst != b:
			b += sign(b_inst - b)
		else:
			if bt < ot and not pause:
				b_inst, bt = get_next_instruction(instructs[1:],'B')
				b_inst = abs(b_inst)
		if ot == bt == 999:
			break
		print time, o,b
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
""")
1 2 1
2 2 1
3 2 1
4 2 1
5 2 1
6 2 1
7 2 1
8 2 1
9 2 1
10 2 1
11 2 1
12 2 1
13 2 1
14 2 1
15 2 1
Traceback (most recent call last):
  File "<pyshell#271>", line 3, in <module>
    """)
  File "<pyshell#227>", line 4, in parse_text
    print [solve_puzzle(i) for i in t]
  File "<pyshell#270>", line 26, in solve_puzzle
    print time, o,b
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1246, in write
    self.shell.write(s, self.tags)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1235, in write
    raise KeyboardInterrupt
KeyboardInterrupt
>>> def solve_puzzle(instructs):
	time = 0
	o = 1
	b = 1
	while 1:
		time += 1
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		pause = False
		if o_inst != o:
			o += sign(o_inst - o)
		else:
			if ot < bt:
				#simulate push
				instructs = instructs[1:]
				o_inst, ot = get_next_instruction(instructs,'O')
				pause = True
		if b_inst != b:
			b += sign(b_inst - b)
		else:
			if bt < ot and not pause:
				instructs = instructs[1:]
				b_inst, bt = get_next_instruction(instructs,'B')
				b_inst = abs(b_inst)
		if ot == bt == 999:
			break
		print time, o,b
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
""")
1 2 1
2 2 1
3 3 1
4 4 2
5 4 2
[6, 1]
>>> parse_text("""3
4 O 2 B 1 B 2 O 4""")
1 2 1
2 2 1
3 3 1
4 4 2
5 4 2
[6]
>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
""")
1 2 1
2 2 1
3 3 1
4 4 2
5 4 2
1 2 2
2 3 3
3 4 4
4 5 5
5 5 6
6 6 7
7 7 8
8 8 9
9 8 10
10 7 11
11 6 12
12 5 13
13 4 14
14 3 15
15 2 16
16 1 17
17 0 18
18 0 19
19 0 20
20 0 21
21 0 22
22 0 23
23 0 24
24 0 25
25 0 26
26 0 27
27 0 28
28 0 29
29 0 30
30 0 31
31 0 32
32 0 33
33 0 34
34 0 35
35 0 36
36 0 37
37 0 38
38 0 39
39 0 40
40 0 41
41 0 42
42 0 43
43 0 44
44 0 45
45 0 46
46 0 47
47 0 48
48 0 49
49 0 50
50 0 51
51 0 52
52 0 53
53 0 54
54 0 55
55 0 56
56 0 57
57 0 58
58 0 59
59 0 60
60 0 61
61 0 62
62 0 63
63 0 64
64 0 65
65 0 66
66 0 67
67 0 68
68 0 69
69 0 70
70 0 71
71 0 72
72 0 73
73 0 74
74 0 75
75 0 76
76 0 77
77 0 78
78 0 79
79 0 80
80 0 81
81 0 82
82 0 83
83 0 84
84 0 85
85 0 86
86 0 87
87 0 
Traceback (most recent call last):
  File "<pyshell#276>", line 5, in <module>
    """)
  File "<pyshell#227>", line 4, in parse_text
    print [solve_puzzle(i) for i in t]
  File "<pyshell#273>", line 28, in solve_puzzle
    print time, o,b
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1246, in write
    self.shell.write(s, self.tags)
  File "/usr/lib/python2.7/idlelib/PyShell.py", line 1235, in write
    raise KeyboardInterrupt
KeyboardInterrupt
>>> def solve_puzzle(instructs):
	time = 0
	o = 1
	b = 1
	while 1:
		time += 1
		o_inst,ot = get_next_instruction(instructs,'O')
		b_inst,bt = get_next_instruction(instructs,'B')
		b_inst = abs(b_inst)
		pause = False
		if o_inst != o:
			o += sign(o_inst - o)
		else:
			if ot < bt:
				#simulate push
				instructs = instructs[1:]
				o_inst, ot = get_next_instruction(instructs,'O')
				pause = True
		if b_inst != b:
			b += sign(b_inst - b)
		else:
			if bt < ot and not pause:
				instructs = instructs[1:]
				b_inst, bt = get_next_instruction(instructs,'B')
				b_inst = abs(b_inst)
		if ot == bt == 999:
			break
		#print time, o,b
	return time

>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
""")
[6, 100, 4, 1]
>>> def parse_text(t):
	t = t.replace('B ','-').replace('O ','').split('\n')[1:]
	t = [map(int,i.split(' ')[1:]) for i in t]
	times = [solve_puzzle(i) for i in t if i != []]
	n = 0
	for i in times:
		n += 1
		print "Case #%d: %d" % (n, i)

		
>>> parse_text("""3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
""")
Case #1: 6
Case #2: 100
Case #3: 4
>>> parse_text("""20
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
10 O 26 B 67 O 84 B 66 O 80 B 74 O 91 B 88 O 41 B 51
10 B 42 O 43 B 87 O 88 B 50 O 50 B 68 O 66 B 56 O 79
10 B 100 B 1 B 100 B 1 B 100 B 1 B 100 B 1 B 100 B 1
5 O 26 O 16 O 96 O 51 B 97
9 B 97 B 75 O 33 B 89 B 58 O 10 O 11 B 67 B 12
6 B 19 O 21 B 41 O 43 O 23 B 18
8 B 13 B 66 O 31 O 55 B 64 B 7 O 86 B 40
9 B 70 O 97 B 66 O 54 O 100 O 65 O 100 O 27 O 41
10 O 59 O 15 O 90 O 89 O 81 O 53 B 1 B 17 O 51 B 60
7 O 3 O 25 B 28 O 78 B 73 O 57 B 73
5 B 18 B 87 B 32 B 86 O 77
1 O 1
10 O 6 B 1 O 8 B 1 O 3 B 2 O 2 B 6 O 6 B 6
7 B 59 O 11 O 41 B 96 O 12 O 86 O 84
8 B 38 O 38 B 83 O 83 O 57 B 56 B 41 O 41
10 B 1 B 1 B 1 O 1 O 1 O 1 B 1 B 1 B 1 B 1
7 O 80 B 74 B 53 O 57 B 24 O 68 B 45""")
Case #1: 6
Case #2: 100
Case #3: 4
Case #4: 154
Case #5: 160
Case #6: 1000
Case #7: 165
Case #8: 233
Case #9: 66
Case #10: 186
Case #11: 349
Case #12: 282
Case #13: 103
Case #14: 200
Case #15: 1
Case #16: 23
Case #17: 199
Case #18: 130
Case #19: 10
Case #20: 155
>>> parse_text("""100
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
56 O 19 B 19 O 6 B 5 B 22 O 26 O 13 B 37 O 27 B 23 O 64 B 61 O 21 B 20 B 45 O 47 B 33 O 35 B 18 O 21 B 60 O 63 B 92 O 32 O 3 B 60 O 40 B 95 O 8 B 64 B 86 O 32 B 97 O 22 B 83 O 8 B 47 O 43 O 28 B 31 O 54 B 6 B 47 O 98 O 73 B 76 O 92 B 93 B 67 O 65 O 22 B 21 B 5 O 42 B 34 O 71
58 B 16 O 17 B 60 O 62 B 75 O 47 B 50 O 23 O 57 B 13 B 43 O 90 O 79 B 55 O 100 B 75 B 42 O 66 O 99 B 6 O 56 B 49 B 73 O 83 O 40 B 29 O 52 B 16 B 38 O 77 B 21 O 61 O 41 B 43 B 6 O 1 O 23 B 30 B 65 O 60 B 35 O 31 B 19 O 14 B 60 O 55 O 28 B 30 O 3 B 6 O 47 B 51 B 36 O 30 B 59 O 6 O 49 B 13
77 B 67 B 38 O 83 O 89 O 36 O 21 O 100 O 57 O 84 B 75 B 7 B 87 O 76 B 4 O 91 B 20 B 80 B 19 O 44 O 7 O 49 O 48 O 36 O 43 O 63 O 53 O 82 O 82 O 55 B 76 O 54 O 22 O 48 B 95 B 24 B 22 O 45 B 94 O 67 O 32 O 29 O 36 O 75 B 51 O 27 O 10 B 75 O 46 B 38 B 11 O 8 B 3 B 30 B 88 O 65 B 18 B 45 O 14 B 80 O 91 B 52 O 33 B 55 B 18 O 54 O 73 O 26 O 50 O 33 O 22 B 15 B 90 O 42 B 87 O 27 B 30 O 26
92 O 96 O 84 B 37 O 96 O 87 B 59 B 90 B 84 B 39 B 92 B 36 O 16 B 99 O 48 O 54 B 19 B 61 B 44 O 58 B 95 O 56 B 86 B 21 B 48 B 68 B 35 B 71 O 2 B 42 B 94 O 39 O 27 B 87 B 70 O 71 O 53 O 28 O 31 B 54 O 23 B 95 O 3 O 47 B 35 O 76 O 35 B 11 O 43 B 92 B 92 B 26 O 65 O 91 B 22 B 67 O 89 O 78 B 66 O 21 B 72 O 91 B 64 O 14 B 18 B 94 O 47 B 82 B 85 B 26 O 42 O 69 O 45 O 88 B 20 O 12 O 40 B 5 O 48 O 42 O 92 B 92 O 46 B 83 O 57 B 58 B 30 O 75 B 97 B 11 B 43 O 3 B 13
60 O 35 B 35 O 59 B 12 O 77 B 29 O 47 B 58 B 21 O 86 B 63 O 45 B 85 O 67 O 25 B 40 O 49 B 62 B 46 O 31 O 49 B 66 O 79 B 96 O 34 B 52 O 59 B 27 B 58 O 92 O 57 B 94 O 97 B 54 B 10 O 50 O 73 B 37 O 100 B 62 B 76 O 84 B 89 O 98 B 71 O 82 B 93 O 59 B 54 O 20 B 9 O 64 B 54 O 18 O 40 B 80 B 51 O 7 O 35 B 82
92 B 26 O 60 O 81 O 39 O 59 B 93 O 52 O 78 O 33 B 70 O 12 B 22 O 42 B 92 O 85 B 96 O 48 O 43 O 5 B 83 O 39 B 28 O 37 O 36 B 31 O 30 B 20 B 55 B 49 B 54 O 72 O 19 B 47 O 53 B 41 B 48 B 39 O 93 B 14 O 75 B 27 O 86 O 68 O 10 O 47 O 53 O 68 B 85 O 37 O 71 B 19 B 97 B 31 B 41 O 4 O 69 B 34 B 52 O 24 O 38 O 98 B 32 B 44 B 16 O 41 O 48 B 25 B 77 O 17 B 21 O 66 B 93 B 66 B 69 O 82 B 62 O 31 B 47 B 24 O 3 O 26 O 26 B 42 O 67 O 31 B 35 O 18 B 6 B 5 O 45 B 53 B 70
66 B 34 O 36 B 59 O 59 B 15 O 15 B 49 O 48 O 22 B 22 B 64 O 66 O 94 B 34 B 64 O 61 B 83 O 43 B 52 O 13 O 40 B 82 O 2 B 46 B 25 O 24 B 11 O 10 O 45 B 47 B 29 O 26 O 45 B 7 O 25 B 26 B 69 O 69 B 38 O 39 B 71 O 71 B 89 O 52 O 81 B 56 O 50 B 25 B 9 O 32 B 54 O 77 O 48 B 22 O 85 B 58 O 51 B 25 B 64 O 92 O 62 B 32 O 17 B 76 O 45 B 47
100 O 19 B 68 B 94 O 48 O 67 B 69 B 75 O 88 O 82 O 77 O 1 B 74 B 26 O 39 B 44 B 2 B 77 O 36 O 39 B 72 O 65 B 36 O 1 B 52 B 58 B 19 O 53 O 60 O 98 O 26 B 94 B 37 O 67 B 22 B 16 B 87 O 68 O 51 O 93 B 98 O 98 O 35 B 39 B 99 B 2 O 82 B 42 B 92 O 65 O 74 O 31 B 90 O 67 B 14 O 24 B 17 O 65 B 48 O 46 O 3 B 57 O 2 O 40 O 25 B 48 B 71 B 63 O 67 O 27 B 23 B 36 B 35 B 98 B 73 B 53 B 66 O 50 B 30 O 44 B 86 O 52 B 44 O 70 B 62 O 10 B 96 O 73 B 99 B 34 B 31 O 60 B 93 B 69 B 22 O 9 B 39 O 53 B 23 B 46 O 82
98 B 37 O 39 B 25 O 50 O 26 B 50 B 75 O 52 B 41 O 19 O 54 B 77 O 65 B 88 B 56 O 99 O 82 B 75 B 35 O 41 O 2 B 76 B 43 O 38 O 78 B 86 O 93 B 70 B 90 O 71 O 87 B 71 B 91 O 64 B 76 O 79 B 87 O 89 O 75 B 70 B 92 O 99 B 70 O 77 O 42 B 32 O 55 B 21 O 82 B 47 O 58 B 71 B 39 O 23 O 9 B 56 O 38 B 26 O 81 B 67 B 83 O 98 B 44 O 59 O 18 B 87 O 54 B 52 O 99 B 98 B 64 O 61 O 89 B 96 B 74 O 65 B 99 O 90 B 58 O 50 B 72 O 64 B 86 O 50 O 67 B 66 B 100 O 31 O 75 B 54 O 45 B 25 O 91 B 70 B 39 O 57 O 72 B 56
98 B 30 O 32 B 71 O 72 B 57 O 86 B 92 O 51 B 59 O 17 O 59 B 13 O 95 B 49 B 83 O 57 O 16 B 39 B 16 O 42 B 40 O 19 B 79 O 57 O 12 B 32 O 50 B 71 O 77 B 45 O 94 B 27 O 47 B 72 O 77 B 41 O 40 B 77 O 4 B 42 O 49 B 86 O 21 B 58 O 52 B 28 B 2 O 79 O 93 B 17 O 76 B 33 O 88 B 46 O 65 B 67 O 50 B 51 B 82 O 15 B 94 O 25 O 39 B 77 O 79 B 38 O 48 B 69 O 74 B 95 O 48 B 69 O 6 B 27 B 17 O 17 B 33 O 33 B 17 O 50 B 43 O 76 B 70 O 51 B 59 O 62 O 86 B 34 O 67 B 53 B 8 O 19 O 5 B 26 O 49 B 69 O 10 B 31
51 O 93 B 68 B 55 O 85 O 19 O 49 B 29 O 91 O 42 B 70 O 29 O 91 B 9 B 76 O 16 O 46 O 8 O 48 O 88 B 15 B 27 B 10 B 39 B 59 O 98 B 69 B 71 O 23 O 58 B 18 B 83 O 19 B 53 B 31 O 96 B 43 O 35 B 10 B 83 O 93 O 24 O 94 O 7 B 95 B 22 O 37 O 81 O 20 B 45 B 10 B 13
56 B 92 O 68 B 62 B 95 O 75 O 20 B 29 O 70 B 87 B 49 O 63 O 89 B 47 O 3 O 47 B 70 B 72 O 96 O 96 B 9 B 22 B 77 O 58 B 66 B 15 B 94 B 57 O 29 O 17 O 60 O 81 B 99 O 27 B 38 B 47 B 89 O 80 B 31 O 33 B 23 O 65 O 15 B 48 O 90 B 64 B 11 O 67 O 72 O 56 B 6 B 78 B 17 B 16 B 62 B 81 B 89
64 B 38 O 38 O 22 B 57 O 37 B 72 B 32 O 80 B 71 O 40 B 46 O 63 O 49 B 63 O 22 B 37 O 9 B 51 B 29 O 33 B 14 O 19 B 1 O 6 B 39 O 45 O 10 B 78 B 96 O 31 B 53 O 75 O 36 B 95 B 65 O 68 B 31 O 34 O 71 B 71 B 33 O 29 O 61 B 69 O 27 B 35 O 74 B 80 B 53 O 44 O 21 B 28 O 41 B 49 B 36 O 25 B 24 O 13 B 49 O 37 B 76 O 63 O 32 B 43
86 O 45 B 46 O 80 B 82 O 54 B 56 B 41 O 35 B 11 O 5 B 33 O 25 O 63 B 72 O 41 B 50 O 10 B 81 O 53 B 37 O 24 B 64 B 76 O 38 B 93 O 55 O 13 B 50 B 85 O 51 O 76 B 56 O 29 B 11 B 46 O 66 B 13 O 34 O 4 B 45 O 39 B 11 O 17 B 32 O 35 B 15 O 14 B 35 B 23 O 29 O 39 B 35 B 4 O 71 O 47 B 30 B 69 O 5 B 23 O 50 B 47 O 25 B 89 O 65 B 60 O 93 O 58 B 97 B 84 O 74 O 100 B 54 B 28 O 70 B 69 O 30 O 15 B 53 O 38 B 77 B 47 O 70 O 25 B 95 B 53 O 70
70 O 26 B 5 B 14 O 71 B 4 O 30 B 52 O 2 O 47 O 57 O 39 O 36 O 57 B 95 O 12 O 74 O 96 O 65 O 58 B 51 O 57 B 27 B 54 B 28 B 4 B 5 O 23 O 89 O 59 B 6 B 97 B 21 O 58 B 75 O 15 B 50 O 82 O 77 B 79 O 50 B 29 O 6 B 49 B 94 B 43 B 69 O 27 B 23 B 5 B 94 O 37 B 25 B 65 B 27 B 61 B 73 B 9 O 40 B 23 O 29 O 94 B 98 O 45 O 64 O 37 B 100 B 75 B 81 B 95 O 65
84 O 42 B 42 B 64 O 19 B 83 O 38 O 9 B 52 O 53 B 9 B 23 O 70 B 49 O 95 B 22 O 67 O 23 B 69 O 6 B 87 O 37 B 56 B 92 O 75 O 39 B 55 O 7 B 22 O 33 B 46 B 4 O 78 O 34 B 50 B 38 O 20 B 49 O 8 O 28 B 73 O 70 B 33 B 13 O 92 O 68 B 39 O 81 B 25 B 56 O 47 B 86 O 18 B 47 O 58 B 64 O 43 B 36 O 71 B 14 O 50 B 45 O 81 B 63 O 63 B 43 O 84 O 65 B 21 B 66 O 18 O 40 B 90 O 86 B 45 O 68 B 64 B 83 O 91 B 51 O 61 O 35 B 22 B 55 O 72
50 O 40 B 40 B 18 O 16 O 32 B 37 B 14 O 6 B 54 O 47 B 92 O 85 B 53 O 46 O 82 B 15 O 47 B 49 O 21 B 22 O 52 B 52 O 88 B 88 B 47 O 46 B 28 O 64 B 62 O 30 B 43 O 50 O 11 B 2 B 17 O 27 O 7 B 39 O 51 B 83 O 83 B 50 B 38 O 98 O 54 B 85 O 80 B 61 O 54 B 34
92 O 21 B 22 B 62 O 62 O 32 B 95 O 18 B 81 O 49 B 52 O 72 B 76 B 37 O 29 B 74 O 64 B 34 O 25 O 69 B 79 B 60 O 90 O 78 B 75 B 42 O 41 B 80 O 77 O 64 B 94 B 83 O 77 B 44 O 39 B 83 O 77 B 63 O 58 B 48 O 74 B 14 O 42 O 83 B 58 O 51 B 90 O 11 B 51 B 79 O 40 B 91 O 51 B 80 O 41 B 62 O 60 O 78 B 41 B 60 O 56 B 98 O 19 O 43 B 71 B 85 O 27 O 53 B 57 B 33 O 79 O 46 B 68 O 90 B 23 B 1 O 64 O 42 B 25 O 30 B 13 O 13 B 30 O 27 B 17 O 55 B 44 B 54 O 43 B 94 O 84 O 55 B 62
52 O 35 B 36 O 81 B 83 O 41 B 43 O 63 B 63 B 77 O 48 B 43 O 15 B 75 O 48 B 35 O 87 B 70 O 51 B 36 O 83 B 76 O 44 O 32 B 62 B 43 O 10 O 32 B 18 B 38 O 55 O 28 B 68 O 72 B 25 O 40 B 58 O 81 B 17 B 59 O 36 B 22 O 74 B 65 O 33 B 93 O 5 O 20 B 76 O 64 B 32 B 2 O 31
100 O 1 B 1 B 1 B 1 O 1 B 1 B 1 O 1 O 1 O 1 B 1 B 1 O 1 O 1 B 1 O 1 O 1 O 1 O 1 B 1 B 1 O 1 B 1 B 1 B 1 B 1 O 1 B 1 O 1 O 1 O 1 B 1 B 1 O 1 B 1 B 1 O 1 O 1 B 1 B 1 O 1 B 1 B 1 B 1 B 1 B 1 B 1 O 1 B 1 B 1 O 1 B 1 O 1 O 1 B 1 B 1 B 1 B 1 O 1 B 1 B 1 B 1 B 1 B 1 O 1 B 1 O 1 B 1 B 1 O 1 B 1 B 1 O 1 O 1 B 1 O 1 O 1 B 1 B 1 B 1 B 1 O 1 O 1 O 1 O 1 B 1 B 1 O 1 O 1 B 1 O 1 B 1 B 1 B 1 O 1 B 1 B 1 O 1 B 1 B 1
66 O 14 B 86 O 87 O 88 O 17 O 90 B 6 O 66 B 57 B 12 O 2 O 36 O 19 B 57 B 75 B 14 B 31 B 41 B 94 O 4 B 40 B 69 B 71 B 5 O 74 B 76 B 96 B 96 B 9 B 14 B 90 O 65 B 83 B 22 O 80 O 89 O 53 B 11 O 53 O 58 O 8 O 76 B 27 O 37 B 100 O 46 B 12 B 94 B 40 B 67 B 30 B 74 O 78 O 88 B 64 B 48 B 52 O 24 B 55 O 1 O 90 B 32 B 70 O 42 O 35 B 73
78 O 41 B 41 B 58 O 60 O 74 B 73 B 84 O 86 B 51 O 53 B 7 O 96 B 34 O 70 O 92 B 57 O 56 B 94 O 87 B 64 O 45 B 21 O 81 B 57 O 57 B 33 B 58 O 29 B 33 O 54 O 91 B 72 B 54 O 70 O 38 B 18 O 79 B 58 B 46 O 66 B 70 O 43 B 35 O 7 B 17 O 25 B 31 O 37 B 54 O 59 O 25 B 18 B 63 O 71 B 49 O 85 O 51 B 84 O 23 B 57 O 64 B 99 B 63 O 25 B 39 O 50 O 86 B 79 B 50 O 53 O 89 B 11 O 47 B 54 B 18 O 8 B 43 O 34
74 B 5 B 80 O 89 O 73 O 82 B 41 O 51 O 99 B 63 B 17 B 96 B 44 O 100 B 68 B 88 O 35 O 20 B 1 B 30 O 15 B 21 O 81 O 30 B 17 B 72 B 53 B 6 O 18 B 90 O 55 B 55 B 78 O 12 O 22 O 30 O 44 O 56 B 28 B 67 B 49 B 64 B 32 O 92 O 43 O 5 B 1 B 54 B 99 B 50 B 20 B 32 B 7 B 27 B 18 B 1 O 37 B 79 O 14 O 13 B 44 O 72 B 51 O 60 O 73 O 31 O 97 O 4 B 80 B 13 O 75 B 74 B 68 B 87 B 14
76 B 47 O 87 B 86 O 91 B 66 B 10 O 92 B 18 O 43 B 30 B 5 B 79 B 92 O 77 O 5 O 51 B 50 B 45 B 26 B 44 O 1 O 12 B 95 O 75 B 50 O 21 O 88 B 94 B 81 O 6 O 10 O 14 O 50 O 34 O 11 O 74 B 39 O 6 B 36 B 33 B 79 B 88 B 46 O 36 B 72 O 65 O 66 B 82 O 24 O 25 B 73 B 1 B 27 O 20 B 85 O 25 B 80 O 57 B 48 B 29 B 46 O 62 B 68 B 63 O 75 O 57 O 56 O 60 O 57 O 79 O 62 O 99 B 11 B 55 O 19 B 5
86 O 24 B 24 O 50 B 49 B 29 O 72 O 97 B 57 B 38 O 74 B 53 O 87 B 28 O 63 O 18 B 76 O 65 B 29 B 73 O 18 O 2 B 92 B 53 O 44 B 15 O 7 O 40 B 51 B 94 O 85 O 69 B 76 B 100 O 42 O 74 B 64 B 41 O 100 B 64 O 77 O 52 B 37 B 52 O 36 B 78 O 11 B 44 O 46 O 28 B 64 B 40 O 3 O 22 B 18 B 54 O 62 B 13 O 22 B 53 O 63 O 86 B 28 B 71 O 41 B 97 O 67 O 80 B 82 O 37 B 39 B 66 O 8 O 38 B 97 B 64 O 4 B 98 O 38 O 15 B 74 B 45 O 47 B 3 O 5 B 21 O 22
72 B 98 B 32 O 23 B 74 B 21 O 55 O 70 B 66 B 16 B 51 O 73 O 90 O 50 B 46 O 46 B 45 B 33 O 69 O 68 O 60 O 97 B 83 B 14 B 40 O 90 O 15 O 80 O 44 O 98 B 34 O 58 B 31 O 49 B 16 B 84 O 74 O 18 O 62 O 92 O 87 O 39 B 11 O 44 B 83 B 45 O 92 O 69 O 2 O 34 B 69 B 49 O 23 B 55 O 89 O 85 B 24 B 7 B 6 B 70 B 17 O 83 B 58 O 8 B 2 O 21 B 64 O 45 O 43 O 74 B 84 B 20 O 50
78 B 20 O 22 O 6 B 2 O 34 B 30 O 15 B 49 O 43 B 20 O 74 B 50 O 55 B 68 B 29 O 95 O 61 B 64 B 90 O 88 B 70 O 67 B 43 O 94 B 20 O 72 B 55 O 36 O 76 B 98 O 47 B 68 B 38 O 15 O 49 B 3 B 17 O 33 O 43 B 5 O 67 B 30 B 68 O 25 O 39 B 84 O 14 B 60 O 52 B 23 B 37 O 69 O 49 B 13 O 29 B 31 O 50 B 52 B 36 O 32 O 77 B 83 O 38 B 44 O 78 B 4 B 32 O 47 B 67 O 81 O 60 B 43 O 21 B 5 O 52 B 36 O 64 B 25
77 O 53 B 86 O 79 O 97 O 33 B 90 O 44 O 58 O 89 O 3 B 33 O 24 O 97 O 41 O 95 B 26 B 46 O 81 B 56 O 6 O 77 B 90 B 76 O 51 B 56 O 32 O 88 B 33 B 13 O 40 O 3 O 51 O 72 O 96 O 8 B 51 O 90 B 45 B 84 O 74 B 45 O 10 O 92 B 37 O 57 O 32 B 17 B 88 B 31 O 81 O 50 O 23 B 47 B 20 O 75 B 78 O 10 B 95 B 41 O 72 O 85 B 18 O 63 B 99 O 88 B 59 B 69 B 90 B 61 B 3 B 8 O 14 B 5 B 46 O 25 O 63 O 43
90 O 18 B 19 O 55 B 57 O 100 B 12 O 78 B 33 B 77 O 33 B 59 O 50 O 13 B 19 B 39 O 36 O 73 B 78 B 90 O 87 O 76 B 78 O 35 B 37 O 79 B 81 O 98 B 61 B 75 O 80 O 48 B 39 O 83 B 4 O 57 B 28 O 97 B 68 O 74 B 44 B 28 O 93 B 2 O 68 O 78 B 14 O 62 B 29 O 42 B 49 O 19 B 26 O 42 B 3 O 84 B 44 B 83 O 44 O 58 B 66 O 28 B 94 O 73 B 49 O 29 B 92 B 78 O 14 B 45 O 46 O 62 B 63 O 26 B 28 O 72 B 73 B 87 O 57 B 56 O 87 O 55 B 91 B 77 O 72 B 46 O 40 O 55 B 65 O 19 B 29
95 B 17 O 100 B 43 B 21 O 80 O 88 B 66 O 19 B 36 B 15 B 4 O 48 B 89 O 66 B 40 O 22 O 38 B 5 O 24 B 17 B 6 O 5 B 68 B 88 B 70 B 33 B 93 B 81 B 97 O 15 B 10 O 84 O 49 B 31 B 51 B 22 O 62 O 69 O 84 O 100 B 84 B 99 B 60 B 30 B 47 B 77 O 36 O 50 B 8 O 15 B 94 B 80 B 95 B 37 B 98 O 56 O 47 O 26 B 25 O 28 B 15 O 32 O 28 B 57 O 58 B 11 B 4 O 97 B 92 O 79 O 12 B 56 O 54 O 90 B 62 O 81 B 96 O 88 O 86 B 46 O 38 B 94 O 30 B 96 B 9 O 75 B 32 O 78 O 35 B 13 O 83 B 17 B 44 O 9 O 5
60 B 19 O 19 O 59 B 61 B 24 O 99 B 66 O 59 O 48 B 80 B 49 O 13 B 94 O 56 O 89 B 58 O 46 B 16 B 41 O 74 B 2 O 37 O 75 B 41 B 71 O 44 O 89 B 23 B 52 O 56 O 100 B 6 B 24 O 80 O 69 B 10 B 43 O 33 B 57 O 18 B 10 O 65 O 96 B 45 B 18 O 65 B 60 O 25 O 43 B 40 B 85 O 91 B 57 O 63 O 74 B 43 O 100 B 18 O 62 B 56
100 O 63 B 35 B 74 B 80 O 19 O 18 B 3 O 25 B 68 O 91 B 46 O 35 O 72 O 59 O 41 O 81 O 49 O 86 B 37 O 53 B 89 B 62 B 17 B 67 B 30 B 12 B 92 O 78 O 83 B 27 O 71 B 63 O 71 B 17 B 28 B 28 O 37 B 61 B 26 O 77 B 39 B 71 O 6 B 84 O 52 O 61 B 26 B 28 B 95 O 8 O 76 O 40 B 77 O 59 B 85 O 90 O 92 B 41 B 94 B 56 O 9 O 74 B 12 O 90 B 43 B 80 O 53 O 65 B 49 B 1 B 33 B 37 O 96 B 63 O 23 B 49 B 94 B 82 B 80 B 60 O 25 B 96 O 60 O 29 O 65 O 69 B 28 O 67 B 4 B 15 O 45 B 95 O 14 O 23 B 43 B 95 O 31 O 26 B 28 O 69
60 O 31 B 31 O 48 B 13 B 41 O 80 B 79 O 44 O 13 B 47 O 47 B 81 O 26 B 60 O 2 B 37 O 29 B 9 B 29 O 5 O 24 B 7 B 32 O 51 B 43 O 61 O 18 B 88 O 52 B 54 O 38 B 67 B 92 O 11 O 21 B 79 B 67 O 6 O 19 B 51 B 23 O 50 B 49 O 75 O 32 B 4 B 30 O 5 B 66 O 42 O 19 B 40 O 54 B 4 B 20 O 74 B 46 O 98 O 72 B 74
64 O 44 B 44 O 79 B 8 O 48 B 39 B 83 O 95 B 56 O 69 B 95 O 31 B 62 O 65 O 50 B 45 B 20 O 76 B 37 O 60 O 38 B 14 B 29 O 22 O 49 B 59 B 14 O 98 B 45 O 68 O 96 B 14 B 26 O 80 B 65 O 42 O 84 B 20 O 54 B 49 B 33 O 35 B 67 O 69 B 97 O 99 B 72 O 74 O 38 B 34 O 4 B 69 O 19 B 56 B 34 O 42 B 8 O 17 B 28 O 37 O 8 B 59 O 43 B 94
1 O 1
80 O 32 B 32 O 64 B 65 B 39 O 94 O 53 B 82 B 71 O 41 B 27 O 86 O 46 B 71 B 57 O 63 B 44 O 77 B 20 O 100 O 68 B 54 O 88 B 73 B 43 O 55 B 55 O 65 B 66 O 75 O 93 B 86 B 44 O 49 B 64 O 28 O 44 B 83 B 52 O 77 O 90 B 68 O 76 B 55 B 94 O 35 B 56 O 74 B 83 O 100 O 88 B 70 B 36 O 53 B 62 O 26 B 98 O 60 B 79 O 42 O 83 B 37 B 60 O 59 B 49 O 49 O 12 B 87 B 65 O 36 B 51 O 50 O 92 B 94 B 55 O 51 O 30 B 78 B 39 O 71
98 O 42 B 44 B 9 O 81 O 57 B 35 B 76 O 100 B 96 O 81 O 41 B 55 O 23 B 36 B 17 O 44 O 85 B 59 B 82 O 61 B 59 O 84 B 17 O 43 B 51 O 77 O 55 B 75 O 91 B 38 O 77 B 50 B 76 O 49 B 57 O 29 O 67 B 17 B 47 O 36 B 84 O 73 B 52 O 41 B 38 O 26 O 59 B 2 O 75 B 18 O 39 B 54 O 55 B 37 B 74 O 94 O 54 B 33 B 76 O 9 O 43 B 41 O 72 B 11 B 30 O 49 B 60 O 78 O 34 B 14 O 68 B 47 O 46 B 26 B 40 O 30 B 86 O 77 O 38 B 44 B 12 O 3 B 33 O 22 B 69 O 59 O 48 B 83 O 61 B 95 B 81 O 76 O 40 B 43 B 7 O 2 B 45 O 41
62 B 64 B 30 B 27 B 74 B 75 B 16 O 100 O 6 O 1 O 62 B 10 O 56 B 31 B 1 B 70 B 45 O 95 B 7 O 78 O 54 O 30 B 71 B 85 B 85 B 95 O 85 B 50 O 21 B 42 B 11 O 48 B 90 O 38 B 67 O 50 B 61 O 52 O 73 O 75 O 84 B 18 O 62 O 73 B 50 B 65 O 45 O 24 O 47 B 25 O 7 O 66 B 44 B 6 B 69 B 100 O 57 O 25 B 13 O 55 O 27 B 56 O 32
76 B 44 O 45 O 33 B 58 B 68 O 46 B 33 O 81 B 77 O 37 B 51 O 11 B 91 O 49 O 32 B 71 O 17 B 58 O 38 B 79 B 43 O 76 B 54 O 87 O 76 B 67 O 95 B 86 O 64 B 54 O 22 B 13 O 36 B 26 B 55 O 5 O 40 B 17 B 7 O 28 O 42 B 23 B 59 O 3 O 38 B 96 B 85 O 24 B 66 O 41 O 52 B 79 O 77 B 53 B 64 O 90 B 39 O 66 B 3 O 29 O 69 B 46 B 1 O 21 B 23 O 42 O 6 B 61 O 30 B 85 B 75 O 18 B 34 O 59 B 74 O 20
55 B 2 B 64 B 26 B 64 B 97 O 30 O 8 B 60 B 96 O 52 B 23 O 60 O 89 B 94 B 84 O 66 O 47 B 63 B 33 B 90 O 49 O 15 B 96 O 68 B 80 B 1 B 41 O 28 B 24 O 80 O 48 O 47 B 83 O 22 B 23 B 94 B 46 O 92 B 100 B 51 O 46 O 41 B 25 O 89 B 53 B 61 B 89 O 32 B 48 O 39 B 99 B 26 B 66 O 33 O 22
73 O 42 O 7 B 84 B 49 B 13 O 93 B 55 B 72 B 75 B 79 B 84 B 13 O 68 B 45 B 89 O 27 O 15 B 59 B 53 O 11 B 15 O 47 B 30 O 6 B 81 B 8 B 61 B 67 B 42 B 9 O 57 O 51 B 11 O 1 B 65 O 20 O 80 B 19 O 59 B 19 O 77 B 31 O 45 O 63 B 22 B 85 O 76 B 60 O 48 B 61 B 82 B 83 O 14 B 20 O 9 B 78 B 76 B 77 O 62 B 66 O 74 B 43 O 35 B 21 O 97 O 11 B 67 B 93 O 74 O 68 O 77 O 66 O 66
86 O 15 B 15 O 38 B 39 O 84 B 85 B 43 O 38 B 1 O 79 B 12 O 89 O 78 B 24 O 54 B 48 O 71 B 30 B 9 O 96 O 83 B 26 O 55 B 54 B 78 O 27 O 70 B 31 O 23 B 77 O 53 B 47 O 40 B 60 B 86 O 67 O 30 B 48 B 30 O 11 B 2 O 38 O 25 B 18 O 59 B 51 B 86 O 96 B 52 O 62 O 25 B 14 O 47 B 37 O 59 B 49 O 40 B 68 B 32 O 80 B 51 O 98 B 86 O 62 B 42 O 18 O 53 B 81 O 30 B 60 B 80 O 8 B 57 O 31 B 81 O 7 O 37 B 49 B 70 O 59 O 15 B 23 O 39 B 45 B 2 O 84
77 B 86 O 91 B 67 O 80 O 94 O 19 O 19 B 78 O 15 O 51 O 75 B 91 B 71 O 18 B 94 O 32 B 88 O 28 B 69 O 3 B 31 B 5 B 13 B 38 O 82 B 67 O 63 B 79 B 6 O 16 O 35 O 8 O 78 B 96 O 9 O 63 B 4 O 16 O 76 O 84 B 52 O 48 B 79 O 25 O 85 O 79 B 98 B 43 O 44 O 22 B 40 B 69 B 56 B 82 O 43 B 85 O 13 B 8 B 26 B 59 O 96 O 80 O 24 O 37 B 49 B 59 B 82 O 60 O 10 O 25 B 34 O 34 B 80 O 11 B 16 B 54 O 49
53 O 86 B 19 O 82 O 81 O 45 O 75 O 72 B 89 B 37 B 80 B 19 O 7 B 91 O 93 O 13 O 3 B 7 B 10 B 17 O 98 O 73 B 50 O 63 O 73 B 18 B 35 O 53 B 26 O 71 O 86 B 88 B 49 B 16 O 92 O 10 B 31 O 64 O 95 B 100 B 34 O 22 B 2 B 58 O 56 B 54 O 14 O 38 O 64 O 74 O 15 B 93 O 28 O 67
78 O 27 B 29 O 10 B 46 O 23 B 35 O 54 B 5 B 22 O 35 O 70 B 60 B 97 O 29 O 41 B 83 B 45 O 82 O 45 B 6 B 32 O 73 O 28 B 78 O 58 B 48 O 99 B 8 O 72 B 36 B 81 O 23 B 52 O 51 O 13 B 92 O 40 B 66 B 25 O 83 O 42 B 68 B 93 O 14 B 64 O 41 O 23 B 43 O 46 B 22 B 50 O 77 B 38 O 66 O 29 B 76 O 64 B 40 O 76 B 30 B 41 O 90 B 10 O 61 O 25 B 49 O 61 B 13 B 30 O 42 O 25 B 11 O 54 B 39 B 76 O 94 B 98 O 73
76 B 42 O 42 B 65 O 19 O 43 B 90 O 72 B 61 O 29 B 18 O 69 B 59 B 91 O 33 B 72 O 51 B 92 O 71 B 78 O 56 B 66 O 44 B 23 O 1 O 33 B 58 B 91 O 69 O 32 B 51 B 79 O 61 O 33 B 50 B 90 O 76 O 99 B 64 O 60 B 26 O 15 B 72 B 30 O 59 O 25 B 67 B 84 O 5 O 50 B 37 O 95 B 82 O 62 B 50 O 40 B 28 B 3 O 13 O 33 B 25 B 68 O 77 B 94 O 51 O 40 B 82 B 58 O 15 B 38 O 34 B 70 O 65 O 41 B 96 O 22 B 76
52 B 21 O 27 O 48 O 19 O 67 B 50 O 65 B 12 O 26 B 43 O 63 B 75 B 54 O 49 O 27 O 6 O 79 B 73 B 22 B 61 O 53 B 12 O 56 B 16 B 16 B 70 O 3 B 92 O 3 B 62 O 66 B 90 O 14 B 31 O 74 O 11 O 36 B 71 O 12 O 85 O 57 B 69 B 10 O 37 O 47 O 76 B 10 O 29 B 53 B 90 O 79 B 96
57 B 95 O 42 O 91 B 71 B 7 B 46 B 100 O 34 B 83 O 46 B 2 O 98 B 3 O 7 B 48 O 10 O 43 B 94 O 92 B 70 O 58 B 17 O 77 B 35 B 83 O 56 O 47 B 36 B 93 O 58 B 59 B 21 O 77 O 32 B 47 O 5 B 7 B 41 B 74 O 1 O 97 O 91 B 17 B 67 O 29 B 12 O 28 O 23 B 100 B 33 O 36 B 79 O 29 O 88 B 80 O 37 B 41
85 O 9 O 36 O 31 B 7 B 75 B 92 O 100 B 47 O 80 B 89 B 15 B 91 B 93 B 36 O 52 B 28 B 81 O 24 B 41 B 46 O 62 O 52 O 66 O 52 O 88 O 20 O 63 O 14 O 45 O 43 O 20 B 85 O 87 B 21 O 66 O 98 O 62 B 85 O 82 B 55 O 78 B 85 O 89 B 34 O 23 O 21 B 53 B 82 O 53 O 95 O 9 B 31 B 88 O 41 O 96 O 43 O 35 O 3 B 73 O 70 O 77 O 15 O 96 O 14 B 16 B 37 B 98 O 23 B 43 B 90 O 60 B 1 O 26 B 49 O 58 O 60 O 85 O 11 O 79 B 14 B 58 B 14 O 88 O 90 B 5
66 O 14 B 14 O 41 B 41 O 2 B 3 O 39 B 41 B 52 O 53 O 10 B 98 O 31 B 79 B 48 O 63 B 4 O 19 B 31 O 46 B 75 O 90 O 48 B 30 O 14 B 64 O 36 B 42 B 1 O 80 O 46 B 36 B 2 O 81 B 26 O 58 B 71 O 14 O 31 B 89 O 65 B 54 O 79 B 66 B 23 O 34 B 51 O 7 O 30 B 75 B 51 O 56 B 85 O 89 O 71 B 66 B 24 O 26 B 6 O 8 O 38 B 38 B 15 O 64 B 56 O 23
96 O 29 B 31 B 75 O 77 O 46 B 40 B 71 O 13 O 27 B 54 O 58 B 23 B 43 O 82 O 52 B 11 B 47 O 90 O 63 B 76 O 84 B 98 O 43 B 59 B 36 O 69 B 55 O 86 O 59 B 85 B 75 O 45 O 1 B 28 O 32 B 60 B 26 O 70 O 57 B 11 O 12 B 55 B 35 O 33 O 11 B 60 O 25 B 72 O 7 B 53 B 34 O 28 O 48 B 56 O 8 B 95 B 72 O 33 O 60 B 100 O 83 B 78 O 97 B 91 B 71 O 76 O 52 B 44 B 23 O 29 O 56 B 52 O 40 B 68 O 21 B 48 B 31 O 41 O 71 B 63 B 49 O 87 O 61 B 20 O 17 B 63 O 45 B 91 O 65 B 71 B 50 O 42 O 63 B 28 O 96 B 62
65 O 95 B 31 O 52 B 29 O 9 O 38 B 48 O 35 B 69 B 26 B 16 O 67 O 40 O 34 B 95 B 79 O 66 O 11 O 19 B 54 O 74 B 22 B 68 B 64 B 12 O 36 O 32 O 22 B 21 B 17 B 16 B 99 B 9 B 61 B 8 B 55 O 56 B 30 O 33 O 50 B 25 B 67 O 9 B 93 O 47 O 67 O 74 B 36 B 46 B 18 B 73 O 95 O 69 O 80 B 10 O 86 O 84 O 80 O 36 O 36 B 64 B 59 B 99 O 8 B 84
53 B 73 O 62 O 43 O 1 B 62 O 82 B 91 B 23 B 94 O 16 O 81 O 86 B 56 O 63 B 75 B 31 B 7 B 50 B 96 O 70 O 61 O 65 B 14 B 3 B 24 O 35 O 83 O 40 O 68 O 99 B 93 B 97 O 87 B 77 B 35 O 32 B 49 B 91 O 69 B 38 B 39 B 61 B 93 B 62 B 49 O 85 B 17 O 54 B 8 O 68 O 31 B 82 B 25
92 O 40 B 41 O 27 B 53 O 4 B 29 B 53 O 32 B 79 O 58 O 71 B 62 B 20 O 26 B 49 O 54 B 6 O 97 B 37 O 67 O 32 B 74 O 69 B 36 O 50 B 17 B 43 O 79 B 12 O 48 B 36 O 25 O 55 B 5 O 91 B 42 O 76 B 57 O 44 B 25 O 67 B 46 B 10 O 29 B 49 O 69 B 69 O 87 O 50 B 29 O 37 B 18 O 60 B 42 B 24 O 81 B 3 O 60 B 28 O 36 B 61 O 70 O 37 B 26 B 70 O 83 O 50 B 36 O 89 B 74 O 50 B 35 O 84 B 68 B 25 O 40 O 76 B 62 B 49 O 90 B 10 O 52 O 84 B 44 B 30 O 68 B 69 O 29 B 33 O 65 B 69 O 29
90 B 29 O 30 B 54 O 55 O 44 B 40 O 63 B 22 O 41 B 43 B 2 O 83 O 53 B 34 O 75 B 55 O 40 B 19 O 80 B 58 O 95 B 74 O 57 B 36 B 2 O 19 B 22 O 38 B 67 O 84 B 86 O 66 B 63 O 90 O 64 B 93 O 84 B 73 B 86 O 99 O 56 B 40 B 7 O 92 O 64 B 36 B 79 O 18 B 94 O 33 O 78 B 45 O 40 B 7 O 75 B 40 B 51 O 87 B 27 O 64 B 46 O 83 O 52 B 13 B 49 O 13 B 63 O 26 B 88 O 2 B 73 O 17 B 60 O 3 B 43 O 19 O 6 B 29 B 58 O 38 O 83 B 10 O 70 B 24 B 39 O 88 B 60 O 67 B 100 O 26
68 O 20 B 22 B 56 O 57 B 68 O 46 O 67 B 91 B 51 O 25 O 51 B 78 O 79 B 50 B 16 O 44 O 55 B 29 O 39 B 13 O 81 B 55 B 66 O 69 O 45 B 93 O 12 B 60 B 31 O 45 O 87 B 75 O 42 B 30 B 70 O 84 B 91 O 62 B 73 O 44 B 37 O 10 O 43 B 71 B 59 O 28 O 50 B 85 B 67 O 70 B 22 O 25 B 52 O 55 B 87 O 91 O 77 B 70 B 45 O 51 B 10 O 85 B 43 O 52 O 38 B 59 O 22 B 42
60 O 83 O 1 O 75 O 17 B 4 O 97 O 30 B 54 O 2 O 68 B 46 B 39 B 12 O 72 B 61 O 100 O 85 O 68 O 38 O 51 O 5 B 28 O 22 O 55 O 55 O 39 O 48 B 69 B 44 O 66 B 71 B 12 O 20 B 53 O 61 B 57 O 54 B 72 O 5 O 82 O 56 O 88 B 77 O 70 O 89 O 23 O 45 O 52 B 38 O 40 O 33 O 27 B 55 O 76 O 40 B 13 B 54 B 25 O 9 B 63
60 B 12 O 14 O 1 B 27 B 50 O 26 B 93 O 70 O 85 B 75 O 54 B 45 B 58 O 68 O 99 B 26 O 87 B 38 B 61 O 61 B 95 O 28 O 44 B 78 B 57 O 21 O 54 B 23 O 30 B 47 B 23 O 56 O 85 B 55 B 75 O 62 O 91 B 45 O 59 B 78 O 16 B 35 B 62 O 45 B 73 O 33 B 30 O 75 B 65 O 39 B 47 O 55 O 79 B 73 B 44 O 49 B 82 O 11 B 49 O 45
57 B 35 O 20 O 19 O 13 O 47 O 95 O 93 O 56 B 95 O 15 B 8 B 17 O 32 B 25 O 38 O 81 O 7 B 5 O 14 B 12 O 84 O 90 B 17 O 70 O 65 B 36 O 97 B 58 B 18 B 95 B 5 O 66 O 1 O 79 B 74 B 48 O 99 O 8 O 20 B 82 O 38 B 26 O 41 O 96 B 69 O 4 B 93 O 96 O 25 O 45 B 15 B 63 B 4 B 5 B 59 B 60 O 76
54 O 30 B 31 B 48 O 11 O 46 B 85 O 5 B 44 O 36 B 14 O 77 B 56 B 21 O 38 B 51 O 66 O 36 B 84 O 73 B 48 O 42 B 16 B 29 O 26 B 7 O 48 B 20 O 34 B 42 O 13 B 56 O 27 B 92 O 63 B 52 O 23 B 70 O 4 O 27 B 96 O 71 B 52 B 85 O 37 O 77 B 42 B 70 O 45 O 30 B 52 B 31 O 54 B 75 O 12
66 O 12 B 12 O 25 B 26 B 65 O 66 O 92 B 93 B 74 O 71 O 28 B 29 B 42 O 42 O 59 B 62 B 43 O 37 B 7 O 2 O 36 B 44 O 60 B 66 B 21 O 13 B 66 O 59 O 40 B 88 B 45 O 86 B 19 O 61 B 52 O 27 O 37 B 65 O 8 B 93 O 21 B 81 O 52 B 49 O 80 B 21 B 5 O 98 B 27 O 75 O 36 B 69 B 96 O 66 B 49 O 20 B 14 O 54 O 11 B 58 O 49 B 20 B 46 O 76 B 17 O 48
100 O 3 B 2 O 2 B 10 O 6 B 4 O 2 B 3 O 3 B 10 O 10 B 3 O 2 B 4 O 3 B 10 O 6 B 1 O 3 B 7 O 9 B 7 O 8 B 10 O 7 B 9 O 9 B 8 O 6 B 4 O 3 B 9 O 3 B 7 O 6 B 2 O 9 B 3 O 5 B 9 O 1 B 1 O 2 B 7 O 6 B 2 O 6 B 10 O 4 B 2 O 9 B 10 O 10 B 8 O 4 B 1 O 6 B 7 O 5 B 3 O 10 B 6 O 6 B 8 O 1 B 3 O 1 B 9 O 4 B 9 O 10 B 1 O 8 B 10 O 1 B 3 O 7 B 8 O 10 B 8 O 1 B 10 O 5 B 4 O 2 B 3 O 10 B 3 O 3 B 2 O 1 B 2 O 4 B 6 O 1 B 1 O 10 B 4 O 3 B 6
84 B 14 B 28 B 50 B 37 O 5 O 82 O 88 O 68 B 70 B 14 O 68 B 25 B 24 B 97 O 7 B 98 O 57 O 70 O 90 B 68 O 26 B 9 B 80 O 73 O 6 O 18 B 90 B 1 B 21 O 98 O 98 O 59 O 95 B 45 B 75 B 68 O 5 B 10 B 18 B 50 B 18 B 36 O 17 O 24 O 74 B 24 B 21 O 33 B 19 O 6 B 71 B 45 O 28 B 26 B 24 B 69 B 48 B 29 O 7 B 1 B 3 B 57 O 16 B 36 B 77 B 57 O 29 O 76 O 20 O 65 O 28 O 95 B 17 O 76 O 86 B 51 B 13 O 100 O 28 B 76 B 47 O 42 O 56 B 7
92 O 25 B 26 O 39 B 40 B 19 O 62 O 25 B 58 B 19 O 66 O 76 B 32 B 13 O 55 B 46 O 21 O 7 B 29 O 40 B 63 O 78 B 26 B 71 O 32 B 51 O 53 O 75 B 26 O 42 B 58 B 72 O 26 B 33 O 65 B 73 O 26 B 43 O 55 B 75 O 88 O 99 B 90 O 53 B 46 B 22 O 28 B 63 O 70 O 83 B 47 B 6 O 40 O 81 B 48 B 37 O 94 B 21 O 79 O 42 B 61 O 76 B 95 B 77 O 54 O 87 B 41 O 69 B 24 B 49 O 43 O 15 B 19 O 46 B 49 O 27 B 29 O 15 B 41 O 60 B 84 B 40 O 14 O 41 B 70 O 61 B 52 B 72 O 82 O 39 B 27 B 68 O 82
94 O 36 B 36 B 53 O 18 O 46 B 24 B 5 O 66 B 48 O 22 O 54 B 12 B 33 O 29 B 7 O 54 B 24 O 36 O 62 B 54 B 24 O 28 O 16 B 38 O 3 B 24 O 17 B 10 O 29 B 22 O 44 B 7 O 7 B 44 O 25 B 61 B 19 O 69 O 82 B 5 O 38 B 49 O 83 B 94 B 58 O 44 O 67 B 85 B 57 O 97 B 78 O 76 B 60 O 93 O 59 B 25 B 4 O 35 B 49 O 80 B 87 O 44 O 18 B 59 B 73 O 3 O 35 B 38 O 76 B 78 B 40 O 35 O 79 B 87 O 44 B 53 B 19 O 80 B 48 O 50 B 85 O 15 B 41 O 60 O 22 B 82 B 38 O 68 O 42 B 9 B 35 O 14 B 79 O 57
100 O 37 B 39 O 64 B 13 B 39 O 91 O 65 B 11 B 44 O 100 O 89 B 30 O 57 B 62 O 88 B 33 O 49 B 73 O 37 B 61 O 51 B 74 O 13 B 35 O 51 B 72 B 83 O 38 B 59 O 15 O 45 B 90 B 68 O 70 O 38 B 32 O 85 B 78 B 89 O 99 O 78 B 64 B 23 O 34 B 35 O 46 O 83 B 75 O 66 B 58 O 41 B 33 B 73 O 84 B 58 O 100 B 31 O 74 O 40 B 66 O 10 B 97 O 33 B 76 B 48 O 2 O 14 B 34 O 45 B 4 O 63 B 21 B 34 O 47 O 86 B 77 B 44 O 51 O 26 B 72 O 39 B 60 B 21 O 80 B 50 O 50 O 77 B 20 B 5 O 61 O 19 B 50 O 41 B 28 O 7 B 60 B 22 O 46 B 64 O 5
84 B 22 O 23 O 64 B 65 O 25 B 27 O 3 B 49 O 26 B 71 O 71 B 26 O 57 B 11 B 29 O 37 B 48 O 55 O 19 B 9 O 58 B 47 O 100 B 6 B 41 O 63 O 24 B 83 B 71 O 38 O 64 B 100 B 79 O 88 O 76 B 64 B 26 O 34 B 56 O 62 B 20 O 99 O 60 B 63 O 17 B 22 B 4 O 36 O 76 B 47 B 19 O 46 B 65 O 92 B 92 O 64 O 39 B 63 B 25 O 81 O 92 B 40 O 64 B 68 O 48 B 82 O 88 B 43 B 28 O 70 B 75 O 25 O 68 B 31 B 74 O 22 B 34 O 61 B 71 O 97 O 67 B 40 O 97 B 70
52 B 27 O 28 B 44 O 12 B 82 O 50 O 7 B 38 O 32 B 12 B 32 O 54 O 76 B 8 B 50 O 32 O 15 B 70 O 35 B 51 B 61 O 22 O 45 B 86 B 76 O 33 B 48 O 6 O 23 B 66 O 62 B 26 B 67 O 19 B 33 O 52 O 31 B 9 O 50 B 27 O 7 B 70 O 20 B 82 O 41 B 61 O 10 B 30 B 66 O 48 B 86 O 67
100 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1 O 100 O 1
82 O 38 B 40 O 67 B 12 O 29 B 51 O 46 B 35 B 22 O 62 O 23 B 64 O 9 B 51 O 41 B 82 B 44 O 1 B 33 O 11 B 18 O 25 O 58 B 52 O 42 B 35 B 80 O 89 O 62 B 52 B 32 O 83 B 12 O 62 B 57 O 17 O 56 B 98 B 70 O 25 O 42 B 91 B 60 O 76 B 23 O 38 B 50 O 11 O 32 B 26 B 60 O 68 B 74 O 54 O 39 B 56 O 52 B 68 B 34 O 88 O 46 B 79 O 71 B 55 B 39 O 53 B 83 O 97 O 53 B 37 B 52 O 71 B 73 O 50 O 87 B 32 O 56 B 3 O 13 B 47 O 43 B 19
72 B 20 O 22 O 65 B 66 B 29 O 27 O 69 B 72 O 27 B 31 O 56 B 60 B 37 O 32 O 64 B 3 B 13 O 77 O 55 B 37 O 98 B 81 O 66 B 49 O 22 B 6 O 65 B 48 B 81 O 100 O 67 B 46 B 80 O 30 O 42 B 66 O 81 B 28 B 70 O 38 B 49 O 16 B 88 O 53 O 71 B 67 B 49 O 91 B 29 O 72 B 59 O 41 O 28 B 43 O 63 B 8 B 22 O 79 B 45 O 57 B 80 O 22 B 63 O 39 O 20 B 41 O 6 B 29 O 42 B 64 B 32 O 9
86 B 78 B 77 O 87 B 82 B 64 O 32 B 98 B 46 O 13 O 83 B 45 B 43 B 49 B 78 B 96 O 29 B 33 O 79 B 34 O 13 O 21 O 90 O 79 B 37 O 68 O 49 O 8 B 66 B 67 B 6 O 42 B 41 B 100 B 26 B 91 B 50 B 82 O 86 O 72 O 14 O 55 O 51 O 35 B 71 B 3 O 80 O 55 O 29 O 99 O 37 B 4 O 88 B 40 O 9 B 61 B 30 O 44 B 79 O 73 B 89 O 11 B 99 B 90 B 42 O 6 B 65 O 41 B 20 B 90 B 4 B 78 O 22 B 92 B 38 B 25 O 94 O 97 B 87 B 19 O 45 B 46 O 11 B 39 O 37 O 49 O 92
51 B 59 B 99 O 80 O 81 B 85 B 24 B 89 B 62 O 83 B 58 B 60 B 45 O 21 O 30 B 24 O 55 O 72 O 89 B 11 B 58 O 22 O 20 O 42 B 98 O 16 O 77 O 21 O 91 O 71 O 63 O 98 B 87 B 12 B 11 O 3 O 8 B 84 B 72 B 31 B 91 B 51 B 9 B 58 B 28 B 7 O 38 O 82 O 50 B 27 B 40 O 66
64 B 38 O 39 B 71 O 6 O 33 B 100 O 71 B 63 B 85 O 47 O 61 B 68 B 94 O 31 O 5 B 64 B 21 O 52 O 28 B 49 O 57 B 20 O 80 B 41 B 17 O 55 O 18 B 56 O 42 B 80 O 20 B 58 B 48 O 8 B 18 O 39 B 31 O 26 O 71 B 80 B 57 O 98 B 80 O 76 B 45 O 42 B 85 O 1 O 16 B 68 O 57 B 27 B 38 O 71 B 51 O 82 O 53 B 82 B 49 O 89 B 23 O 63 O 25 B 65
82 O 45 B 47 O 67 B 27 B 51 O 41 O 61 B 72 B 32 O 19 B 78 O 66 O 89 B 52 O 63 B 27 B 59 O 28 O 38 B 72 O 17 B 93 B 59 O 54 O 15 B 16 B 40 O 41 O 19 B 15 B 46 O 52 B 13 O 85 O 50 B 49 B 16 O 15 O 38 B 42 O 7 B 73 B 36 O 48 B 77 O 9 B 36 O 50 B 12 O 25 B 24 O 37 O 75 B 65 B 42 O 99 B 9 O 67 O 79 B 23 O 67 B 35 O 78 B 45 O 44 B 12 O 31 B 24 B 49 O 58 O 38 B 26 O 66 B 54 B 36 O 86 O 68 B 16 B 6 O 79 O 36 B 52
98 O 14 B 15 O 45 B 47 O 59 B 61 O 29 B 31 B 1 O 61 B 17 O 76 O 34 B 60 O 71 B 97 B 71 O 44 B 35 O 7 B 6 O 34 B 30 O 9 O 33 B 57 B 98 O 75 O 63 B 84 O 52 B 94 O 30 B 71 B 29 O 75 O 34 B 71 O 47 B 84 B 54 O 16 O 50 B 17 B 47 O 16 O 59 B 94 B 57 O 20 O 10 B 44 B 69 O 37 B 81 O 49 B 46 O 85 B 3 O 44 B 19 O 27 B 44 O 2 B 87 O 44 B 63 O 69 O 89 B 39 B 80 O 45 B 99 O 65 B 75 O 41 B 29 O 85 B 52 O 61 B 12 O 99 O 57 B 55 B 66 O 43 O 8 B 27 O 52 B 70 O 29 B 94 B 49 O 78 O 53 B 77 O 18 B 42
70 O 13 B 13 B 51 O 54 O 19 B 88 B 54 O 55 O 76 B 77 B 88 O 64 B 100 O 53 B 80 O 74 O 42 B 44 O 30 B 33 B 69 O 68 B 30 O 29 O 42 B 15 B 27 O 56 O 74 B 7 B 17 O 85 B 36 O 65 O 22 B 81 O 3 B 62 B 74 O 17 O 57 B 33 O 17 B 73 O 49 B 41 B 63 O 26 B 94 O 56 O 19 B 56 O 34 B 42 B 14 O 5 B 56 O 47 O 78 B 89 O 44 B 55 B 75 O 23 O 56 B 41 B 83 O 12 B 38 O 58
96 B 32 B 61 O 55 B 19 B 24 B 31 O 46 B 48 O 99 O 51 O 87 B 20 O 17 B 53 O 46 O 89 B 3 O 71 O 30 B 59 O 75 B 58 O 100 O 61 B 23 O 28 O 10 B 37 B 3 O 12 B 90 B 96 O 91 O 53 O 100 B 82 O 47 B 78 O 43 O 34 B 69 O 91 O 71 B 30 O 16 O 97 O 28 B 29 B 92 B 11 B 54 B 48 B 97 O 6 O 68 O 29 B 70 O 15 O 1 B 27 B 79 B 27 B 79 B 41 B 46 O 20 B 22 B 95 O 70 O 2 O 34 B 90 O 85 O 91 B 2 O 4 O 46 B 82 O 39 O 24 B 75 B 40 B 84 O 60 B 12 O 29 B 67 B 9 B 10 O 21 B 28 O 38 O 82 O 29 B 28 O 1
88 O 10 O 28 O 63 B 50 B 58 B 100 B 87 O 100 O 15 B 15 B 13 O 57 O 76 O 18 B 36 O 100 O 12 B 87 B 65 B 80 B 77 B 44 B 43 O 73 B 18 O 3 O 8 B 7 B 67 O 100 B 47 O 92 O 86 O 94 O 80 O 33 B 94 O 59 O 87 B 35 O 35 O 33 O 24 B 28 O 87 B 61 B 67 O 23 O 7 B 69 O 41 B 34 B 61 B 73 B 57 O 55 O 96 B 63 B 42 O 8 O 55 B 93 O 70 O 17 B 15 B 76 O 91 B 4 O 38 O 96 B 10 O 83 O 52 B 88 B 95 O 50 B 14 O 66 O 80 B 10 O 92 B 43 O 47 O 93 B 27 O 44 B 70 O 98
86 O 42 B 44 B 20 O 16 B 31 O 27 O 49 B 54 O 61 B 41 B 29 O 47 O 70 B 3 O 27 B 46 O 64 B 83 B 63 O 41 O 84 B 18 O 65 B 37 B 57 O 86 O 55 B 24 B 65 O 97 B 79 O 82 O 44 B 37 B 20 O 65 B 42 O 85 O 69 B 61 B 73 O 85 O 65 B 96 B 67 O 33 B 21 O 78 O 63 B 38 B 63 O 90 O 53 B 24 O 17 B 59 O 56 B 99 O 16 B 60 O 27 B 71 B 33 O 68 B 75 O 27 O 14 B 91 B 60 O 49 B 83 O 72 B 47 O 37 O 59 B 70 B 33 O 99 B 14 O 81 B 37 O 59 B 62 O 33 O 58 B 91
54 O 13 B 13 B 45 O 46 O 88 B 2 O 64 B 26 B 3 O 88 B 33 O 58 B 66 O 26 O 9 B 86 O 36 B 61 O 54 B 42 O 97 B 83 O 60 B 47 B 76 O 30 B 34 O 71 B 20 O 57 B 50 O 88 O 66 B 25 O 94 B 53 O 61 B 87 B 54 O 26 B 27 O 54 B 12 O 68 B 57 O 24 B 98 O 64 O 86 B 75 B 90 O 70 O 35 B 52
62 B 21 O 22 O 65 B 66 O 95 B 36 B 24 O 80 O 39 B 69 O 19 B 51 O 38 B 31 O 1 B 68 O 45 B 25 O 84 B 64 O 54 B 93 B 76 O 35 B 32 O 78 O 41 B 70 B 52 O 22 B 15 O 58 B 2 O 70 O 34 B 39 B 17 O 10 O 29 B 37 O 75 B 84 O 30 B 41 O 74 B 85 B 70 O 58 B 25 O 13 O 33 B 47 O 13 B 27 O 40 B 55 B 97 O 85 B 80 O 69 B 67 O 81
75 O 56 O 11 O 58 O 29 B 66 O 52 B 53 B 57 B 50 B 39 B 50 O 14 O 68 B 44 O 31 O 79 B 2 O 23 O 25 B 54 O 9 O 38 O 72 O 49 B 42 O 15 B 55 O 19 O 66 B 74 B 68 B 8 B 8 O 41 B 24 B 45 B 20 B 8 O 51 B 14 B 61 B 50 O 65 B 75 O 1 O 68 O 74 O 18 B 2 O 37 O 26 B 82 B 50 O 52 B 92 B 73 O 54 O 43 O 4 B 18 B 4 B 50 B 72 B 12 O 89 O 80 B 16 B 88 O 41 B 2 O 50 B 15 O 58 O 65 O 72
58 O 30 B 32 B 63 O 64 B 49 O 49 O 7 B 95 B 62 O 44 B 19 O 3 O 26 B 43 O 7 B 63 O 33 B 88 O 76 B 46 B 74 O 45 O 70 B 47 B 83 O 33 O 7 B 54 O 46 B 91 B 62 O 76 B 34 O 47 B 52 O 63 B 28 O 87 O 71 B 10 B 48 O 31 O 57 B 19 O 12 B 63 O 55 B 20 B 9 O 42 O 86 B 54 B 74 O 65 B 91 O 82 B 70 O 61
85 B 86 B 96 O 12 O 17 O 77 O 78 B 98 B 98 O 49 O 98 B 37 B 19 O 9 B 45 B 63 B 25 B 50 B 88 O 19 B 11 O 99 B 100 O 27 O 8 O 65 B 68 O 63 O 5 B 50 O 50 O 36 B 94 B 22 B 21 B 71 B 95 O 4 O 43 O 91 B 84 O 78 B 51 O 68 O 92 O 2 B 28 O 81 O 32 B 3 O 35 O 62 O 65 O 48 O 10 O 3 B 35 B 33 O 12 O 40 B 51 B 94 B 89 O 4 B 75 O 71 B 96 B 33 B 17 B 29 O 32 B 69 O 85 B 23 O 9 B 14 O 55 O 85 O 33 B 75 O 37 B 27 B 91 O 71 B 44 B 49
78 B 36 O 36 O 79 B 81 B 99 O 100 O 62 B 57 B 45 O 48 B 80 O 82 B 64 O 97 B 86 O 74 B 40 O 29 B 76 O 65 B 43 O 31 B 57 O 18 O 54 B 19 B 48 O 23 B 6 O 64 O 47 B 26 O 89 B 66 B 79 O 73 B 48 O 43 B 20 O 70 O 88 B 40 B 6 O 51 B 38 O 19 B 76 O 55 B 37 O 94 O 53 B 81 B 48 O 88 B 28 O 68 B 43 O 53 B 76 O 19 O 44 B 47 O 20 B 24 O 32 B 11 O 7 B 34 O 42 B 70 O 85 B 28 O 69 B 44 O 85 B 27 O 41 B 69
90 O 23 B 25 B 42 O 44 O 69 B 71 B 26 O 22 O 47 B 54 O 10 B 89 B 57 O 43 O 57 B 72 O 38 B 54 B 42 O 51 B 62 O 72 O 52 B 40 B 66 O 23 B 96 O 52 B 79 O 68 O 32 B 42 O 6 B 69 B 88 O 27 B 45 O 71 B 89 O 27 B 61 O 53 O 40 B 47 B 60 O 24 B 18 O 64 O 46 B 39 O 12 B 5 O 47 B 40 B 50 O 35 B 9 O 77 O 92 B 27 O 66 B 53 B 14 O 26 O 62 B 53 B 38 O 80 O 67 B 24 O 44 B 48 B 77 O 11 B 37 O 49 B 56 O 67 O 28 B 97 B 81 O 46 O 20 B 53 B 69 O 37 O 51 B 52 B 18 O 88
100 O 29 B 33 O 74 B 78 O 25 B 10 O 8 B 62 O 84 B 95 O 70 B 48 O 90 B 51 O 75 B 98 O 4 B 95 O 76 B 10 O 63 B 48 O 77 B 88 O 69 B 19 O 50 B 64 O 34 B 99 O 40 B 18 O 84 B 75 O 45 B 1 O 46 B 29 O 45 B 53 O 48 B 65 O 3 B 12 O 91 B 96 O 84 B 25 O 18 B 53 O 39 B 68 O 58 B 4 O 3 B 39 O 8 B 27 O 17 B 94 O 37 B 36 O 43 B 39 O 55 B 76 O 68 B 44 O 50 B 36 O 40 B 40 O 17 B 71 O 82 B 76 O 91 B 83 O 35 B 90 O 85 B 58 O 94 B 65 O 27 B 32 O 51 B 25 O 48 B 36 O 64 B 23 O 29 B 30 O 60 B 34 O 63 B 49 O 41 B 71
58 O 20 B 22 O 45 B 45 O 90 B 91 B 54 O 50 B 40 O 64 O 27 B 80 O 68 B 40 O 23 B 84 O 68 B 38 O 26 B 80 O 6 B 100 B 65 O 43 B 53 O 55 B 87 O 88 B 71 O 73 B 38 O 41 B 50 O 29 O 12 B 30 O 25 B 41 O 44 B 59 B 20 O 86 B 7 O 74 B 49 O 31 B 70 O 51 O 94 B 24 B 57 O 57 B 83 O 32 B 48 O 67 O 89 B 72
90 O 55 B 85 B 83 B 28 B 12 O 74 B 39 O 86 O 70 O 17 O 62 B 89 O 14 O 62 O 28 O 70 O 17 O 13 B 29 B 93 B 40 O 75 B 79 O 77 O 96 B 73 B 47 B 91 B 74 O 86 B 53 O 27 O 7 B 45 B 14 B 46 O 56 B 82 O 67 O 18 O 74 O 15 B 35 O 93 O 52 O 52 O 28 B 73 O 3 O 35 B 26 O 47 B 27 B 55 O 97 B 1 O 54 O 98 O 67 B 29 O 42 O 99 O 65 B 31 O 23 O 26 O 46 B 97 O 74 B 69 B 76 O 63 O 86 O 59 O 46 O 34 O 64 B 47 O 68 B 74 O 17 O 27 B 88 O 31 O 49 O 86 O 37 O 7 O 29 B 93
64 O 31 B 31 O 47 B 46 B 66 O 25 B 80 O 12 B 50 O 41 B 78 O 69 O 36 B 43 O 57 B 63 B 46 O 77 B 71 O 52 O 95 B 26 B 2 O 68 O 24 B 50 O 1 B 73 O 39 B 37 B 60 O 64 B 91 O 95 B 46 O 50 B 69 O 72 B 41 O 100 O 83 B 61 O 42 B 22 B 3 O 20 O 46 B 32 O 11 B 68 O 37 B 43 O 59 B 65 B 96 O 93 O 55 B 55 O 90 B 21 O 59 B 53 B 84 O 94
54 O 46 B 47 O 17 B 76 B 51 O 44 O 20 B 77 B 36 O 62 O 49 B 51 B 64 O 35 O 74 B 23 O 31 B 66 O 73 B 24 B 59 O 37 O 18 B 81 B 46 O 56 O 24 B 79 B 49 O 56 O 82 B 78 B 44 O 45 O 7 B 85 O 33 B 61 B 42 O 54 O 74 B 21 O 55 B 3 B 30 O 26 O 67 B 72 O 22 B 28 O 67 B 74 O 35 B 43
96 B 24 O 24 B 45 O 44 B 59 O 59 O 36 B 84 B 49 O 73 B 61 O 61 B 29 O 28 O 53 B 58 B 83 O 81 B 56 O 54 B 30 O 80 O 36 B 76 B 38 O 76 B 57 O 56 B 78 O 35 B 55 O 56 B 66 O 45 B 24 O 86 B 59 O 51 B 13 O 5 O 40 B 49 O 85 B 3 B 35 O 49 B 59 O 71 O 40 B 27 B 11 O 58 O 35 B 35 B 80 O 82 O 94 B 67 B 49 O 74 B 11 O 37 O 62 B 39 O 78 B 25 B 57 O 43 O 73 B 90 O 56 B 74 B 89 O 72 O 27 B 41 O 71 B 83 B 58 O 97 O 70 B 88 B 56 O 36 O 10 B 29 O 47 B 67 B 56 O 62 B 70 O 49 B 99 O 79 B 78 O 98
90 O 42 B 44 O 78 B 10 B 34 O 51 B 64 O 21 B 36 O 49 B 10 O 75 B 35 O 50 O 63 B 51 O 21 B 8 O 54 B 40 O 89 B 75 O 53 B 38 B 18 O 77 B 52 O 45 B 71 O 65 B 98 O 39 B 55 O 81 B 84 O 52 B 46 O 90 B 4 O 47 B 19 O 61 B 33 O 74 B 55 O 95 O 73 B 30 O 28 B 74 O 58 B 45 B 21 O 83 O 55 B 51 B 30 O 77 O 32 B 78 O 47 B 65 B 38 O 17 O 38 B 63 O 2 B 27 O 22 B 45 B 33 O 35 B 62 O 6 O 16 B 73 B 91 O 35 O 57 B 67 O 77 B 47 O 46 B 17 O 1 B 62 B 36 O 30 O 74 B 84
98 B 38 O 51 O 97 B 70 O 45 O 97 O 90 O 15 O 66 O 5 B 12 O 93 B 96 B 85 O 58 O 16 O 68 O 42 B 58 B 2 O 78 O 86 B 20 B 15 B 81 O 25 B 81 B 19 O 32 B 54 B 34 B 44 B 78 B 35 B 44 O 95 B 18 O 43 B 39 O 8 O 20 O 92 B 15 O 72 O 88 B 80 O 25 B 12 B 81 O 88 B 12 B 52 O 54 O 94 B 73 O 95 B 48 B 52 O 98 O 32 O 68 O 21 B 59 B 84 B 35 B 49 O 17 O 34 O 33 O 34 B 80 B 80 B 52 O 4 B 88 O 72 O 52 O 45 B 50 B 73 B 59 B 78 B 86 O 87 O 92 B 97 B 6 O 30 B 75 O 22 B 57 O 6 O 82 B 1 O 55 B 85 O 72 O 33
62 B 36 O 38 B 58 O 17 B 26 O 48 O 78 B 57 B 67 O 89 B 28 O 50 B 61 O 18 O 58 B 20 B 8 O 71 O 86 B 24 B 47 O 62 O 86 B 22 B 53 O 52 B 39 O 66 B 61 O 87 O 75 B 74 O 57 B 91 B 51 O 100 O 74 B 21 B 33 O 58 O 20 B 73 B 43 O 52 B 77 O 19 B 97 O 39 B 63 O 5 B 95 O 37 O 76 B 55 O 99 B 33 B 65 O 65 B 24 O 23 B 8 O 37
65 B 96 B 29 B 42 O 20 O 47 B 6 B 5 O 33 O 88 B 34 B 15 O 61 B 82 B 88 O 25 O 95 O 45 B 25 O 47 B 71 O 24 O 100 B 22 B 33 B 95 B 10 O 34 B 86 B 53 B 46 O 75 O 79 O 7 O 46 O 82 O 14 B 57 O 74 B 10 B 95 O 32 B 24 O 62 B 76 O 88 B 4 O 51 B 83 B 49 O 84 B 78 O 57 O 56 O 41 O 20 B 90 O 9 B 84 B 83 O 7 B 86 O 2 O 50 O 60 O 72""")
Case #1: 6
Case #2: 100
Case #3: 4
Case #4: 746
Case #5: 852
Case #6: 1969
Case #7: 2329
Case #8: 929
Case #9: 1837
Case #10: 1044
Case #11: 2295
Case #12: 1409
Case #13: 1460
Case #14: 1538
Case #15: 1511
Case #16: 936
Case #17: 1332
Case #18: 1772
Case #19: 1239
Case #20: 793
Case #21: 1283
Case #22: 867
Case #23: 100
Case #24: 1882
Case #25: 1206
Case #26: 2056
Case #27: 1664
Case #28: 1318
Case #29: 1921
Case #30: 1104
Case #31: 2156
Case #32: 1311
Case #33: 2199
Case #34: 996
Case #35: 2339
Case #36: 815
Case #37: 974
Case #38: 1
Case #39: 1124
Case #40: 1523
Case #41: 1398
Case #42: 1043
Case #43: 1426
Case #44: 1502
Case #45: 1255
Case #46: 1704
Case #47: 1376
Case #48: 1174
Case #49: 1192
Case #50: 1202
Case #51: 1580
Case #52: 2420
Case #53: 1055
Case #54: 1313
Case #55: 1424
Case #56: 1354
Case #57: 1436
Case #58: 1259
Case #59: 974
Case #60: 1557
Case #61: 830
Case #62: 1599
Case #63: 827
Case #64: 995
Case #65: 300
Case #66: 1955
Case #67: 1375
Case #68: 1458
Case #69: 1446
Case #70: 1365
Case #71: 718
Case #72: 10000
Case #73: 1216
Case #74: 1098
Case #75: 2378
Case #76: 1336
Case #77: 933
Case #78: 1181
Case #79: 1498
Case #80: 1001
Case #81: 2643
Case #82: 2067
Case #83: 1228
Case #84: 810
Case #85: 958
Case #86: 1635
Case #87: 886
Case #88: 2142
Case #89: 1186
Case #90: 1246
Case #91: 1997
Case #92: 876
Case #93: 2131
Case #94: 960
Case #95: 885
Case #96: 1387
Case #97: 1330
Case #98: 2462
Case #99: 880
Case #100: 1756
>>> 
