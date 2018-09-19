#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        probA.py
# Purpose:     Solves 2012 Code Jam Qualification Round Problem A
#
# Author(s):   Andre Wiggins
#
# Created:     April 14, 2012
# Copyright:   (c) Andre Wiggins 2012
# License:
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------

DEBUG = False

sample_input = ' '.join(['ejp mysljylc kd kxveddknmc re jsicpdrysi',
                         'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
                         'de kr kd eoya kw aej tysr re ujdr lkgc jv'])
sample_output = ' '.join(['our language is impossible to understand',
                          'there are twenty six factorial possibilities',
                          'so it is okay if you want to just give up'])


def debug(s):
	if DEBUG:
		print s


def build_key():
	key = {}
	for ggl_char, engl_char in zip(sample_input, sample_output):
		if not key.has_key(ggl_char):
			key[ggl_char] = engl_char
		elif engl_char != key[ggl_char]:
			debug("ERROR: build_key(): {} != {}".format(engl_char, key[ggl_char]))

	key['q'] = 'z'
	key['z'] = 'q'
	return key


def main():
	key = build_key()
	debug(key)

	n = input()
	for i in xrange(n):
		ggl_line = raw_input()
		engl_line = ''.join(key[c] for c in ggl_line)
		print "Case #{}: {}".format(i+1, engl_line)


main()
