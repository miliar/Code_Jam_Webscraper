#!/usr/bin/python2

import sys, os, string, re

def make_tree(text):
	content = re.search('[(](.*)[)]', text).group(1)
	groups = content.strip().split()
	if len(groups) == 1:
		return [float(groups[0])]
	sub_content = re.search('([(].*[)])', content).group(1)
	pos = 1
	depth = 1
	while depth > 0:
		if sub_content[pos] == '(':
			depth += 1
		if sub_content[pos] == ')':
			depth -= 1
		pos += 1
	return [float(groups[0]), groups[1],
		make_tree(sub_content[:pos]), make_tree(sub_content[pos:])]

def get_prob(p, tree, attributes):
	p *= tree[0]
	if len(tree) == 1:
		return p
	if tree[1] in attributes:
		return get_prob(p, tree[2], attributes)
	else:
		return get_prob(p, tree[3], attributes)

in_file = sys.stdin
T = int(in_file.readline())
for case_num in range(T):
	L = int(in_file.readline().strip())
	text = ''
	for i in range(L):
		text += in_file.readline()[:-1]+' '
	tree = make_tree(text)
	print('Case #'+str(case_num+1)+':')

	A = int(in_file.readline().strip())
	for i in range(A):
		groups = in_file.readline().strip().split()
		attributes = groups[2:]
		print '%.7f' % get_prob(1.0, tree, attributes)
