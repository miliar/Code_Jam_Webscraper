#!/usr/bin/env python

import sys

def solve(db):
	line = sys.stdin.readline().strip()
	if line == '':
		line = sys.stdin.readline().strip()
	a, b = line.split(' ')
	return db.count_between(a, b)

class DB:
	def __init__(self):
		import sqlite3
		self.conn = sqlite3.connect('fairsq.db')
		self.c = self.conn.cursor()
		self.c.execute('CREATE TABLE IF NOT EXISTS fairsq (num1 int unique not null, num2 int unique not null)')

	def insert(self, rows):
		self.c.executemany('INSERT OR REPLACE INTO fairsq (num1, num2) VALUES (?, ?)', rows)
		self.conn.commit()

	def count_between(self, num1, num2):
		self.c.execute('select count(num1) from fairsq where num1 between ? and ?', (num1, num2))
		return self.c.fetchone()[0]

def is_palindrome(i):
	import math
	len = int(math.ceil(math.log10(i+1)))
	for n in range(len/2):
		if (i / int(math.pow(10, n))) % 10 != (i / int(math.pow(10, len - n - 1))) % 10:
			return False
	return True;

def fill_fairsq(db, num1, num2):
	import math
	to_add = []
	beginning = int(math.ceil(math.sqrt(num1)))
	end = int(math.floor(math.sqrt(num2)))
	for i in xrange(beginning, end):
		if is_palindrome(i) and is_palindrome(i**2):
			to_add.append([i**2, i])
			if len(to_add) > 50:
				db.insert(to_add)
				to_add = []
	if len(to_add) > 0:
		db.insert(to_add)


if __name__ == '__main__':
	db = DB()

	if len(sys.argv) > 1:
		fill_fairsq(db, 1, 10**14)

	T = int(sys.stdin.readline())

	for t in range(T):
		result = solve(db)
		print "Case #%d: %s" % (t+1, result)
